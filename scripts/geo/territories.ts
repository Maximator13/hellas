import { createHash } from 'node:crypto'
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { createRequire } from 'node:module'
import { dirname } from 'node:path'
import { z } from 'zod'
import { fromHistorical } from '../../src/core/dates.ts'
import { TRACK_IDS } from '../../src/data/schema.ts'
import type { Track, TrackId } from '../../src/data/schema.ts'
import { tracks } from '../../src/data/tracks.ts'
import { MAP_BOUNDS } from '../../src/map/geo.ts'

const RELEASE = 'v0.2.1'
const REPOSITORY = 'https://github.com/Seshat-Global-History-Databank/cliopatria'
const ARCHIVE_URL = `https://raw.githubusercontent.com/Seshat-Global-History-Databank/cliopatria/${RELEASE}/cliopatria.geojson.zip`
const ARCHIVE_SHA256 = 'e10a4e429fca708788ff9e7572a95fce801fae55852d217cffabc1c59cd4eed4'
const CACHE = `.cache/geo/cliopatria-${RELEASE}`
export const TERRITORIES_FILE = 'public/geo/territories.json'
export const SIZE_TARGET = 900_000
const ALIGN_YEARS = 5
const BRIDGE_YEARS = 10
const SIMPLIFY_METERS = 27_000
const SMALL_RING_METERS = 8_000
const SMALL_RING_AREA = 5e9
const MIN_ISLAND = '100km2'

interface Mapshaper {
  applyCommands(commands: string, input?: Record<string, string>): Promise<Record<string, string | Uint8Array>>
}

const mapshaper: Mapshaper = createRequire(import.meta.url)('mapshaper')

export const ATTRIBUTION = `J. S. Bennett, E. Mutch, A. Tollefson et al., Cliopatria ${RELEASE} (Seshat Global History Databank), ${REPOSITORY}, licence CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/), modifié (extraction des entités grecques, perses, hellénistiques et romaines, simplification, dates alignées sur le projet, conquêtes d'Alexandre de 331 à 324 av. J.-C. renommées, car étiquetées « Ptolemaic Kingdom » dans la source)`

interface Source {
  polity: string
  track: TrackId
  merge?: boolean
  from?: number
  to?: number
}

const SOURCES: Source[] = [
  { polity: 'Greek Dark Ages', track: 'monde-grec' },
  { polity: 'Greek City-States', track: 'monde-grec' },
  { polity: 'Greek Colonies', track: 'monde-grec' },
  { polity: 'Mycenaean Greece', track: 'myceniens' },
  { polity: 'Minoan civilization', track: 'minoens' },
  { polity: 'Second Athenian League', track: 'athenes' },
  { polity: 'Athenian Coalition', track: 'athenes' },
  { polity: 'Peloponnesian League', track: 'sparte' },
  { polity: 'Achaemenid Empire', track: 'perse' },
  { polity: 'Macedonian Empire', track: 'macedoine', to: -336 },
  { polity: 'Macedonian Empire', track: 'macedoine', from: -300 },
  { polity: 'Antigonid Dynasty', track: 'macedoine' },
  { polity: 'Antigonid Macedonia', track: 'macedoine' },
  { polity: 'Macedonian Empire', track: 'alexandre', from: -335 },
  { polity: 'Ptolemaic Kingdom', track: 'alexandre', merge: true, to: -323 },
  { polity: 'Perdiccas', track: 'alexandre', merge: true },
  { polity: 'Laomedon', track: 'alexandre', merge: true },
  { polity: 'Polyperchon', track: 'alexandre', merge: true },
  { polity: 'Ptolemaic Kingdom', track: 'lagides', from: -322 },
  { polity: 'Seleucid Empire', track: 'seleucides' },
  { polity: 'Roman Republic', track: 'rome' },
  { polity: 'Sacred Band of Thebes', track: 'thebes' },
  { polity: 'Thebans', track: 'thebes' },
  { polity: 'Kingdom of Pergamon', track: 'pergame' },
  { polity: 'Rhodes', track: 'rhodes' },
  { polity: 'Achaean League', track: 'ligues' },
  { polity: 'Aetolian League', track: 'ligues', merge: true },
]

const position = z.tuple([z.number(), z.number()]).rest(z.number())
const geometrySchema = z.discriminatedUnion('type', [
  z.object({ type: z.literal('Polygon'), coordinates: z.array(z.array(position)) }),
  z.object({ type: z.literal('MultiPolygon'), coordinates: z.array(z.array(z.array(position))) }),
])
const cliopatriaSchema = z.object({
  features: z.array(
    z.object({
      properties: z.object({ Name: z.string(), FromYear: z.number().int(), ToYear: z.number().int(), Type: z.string() }),
      geometry: geometrySchema,
    }),
  ),
})
const simplifiedSchema = z.object({ features: z.array(z.object({ geometry: geometrySchema.nullable() })) })
const pointSchema = z.object({ features: z.array(z.object({ geometry: z.object({ type: z.literal('Point'), coordinates: position }) })).min(1) })

const lonLat = z.tuple([z.number(), z.number()])
export const territoriesSchema = z.strictObject({
  attribution: z.string(),
  slices: z.array(
    z.strictObject({
      track: z.enum(TRACK_IDS),
      polity: z.string(),
      from: z.number().int(),
      to: z.number().int(),
      bounds: z.tuple([z.number(), z.number(), z.number(), z.number()]),
      label: lonLat,
      polygons: z.array(z.array(z.array(lonLat))),
    }),
  ),
})

type Geometry = z.infer<typeof geometrySchema>
type LonLat = z.infer<typeof lonLat>
export type Slice = z.infer<typeof territoriesSchema>['slices'][number]

export interface Row {
  polity: string
  from: number
  to: number
  geometry: Geometry
}

export interface Plan {
  track: TrackId
  polity: string
  from: number
  to: number
  rows: Row[]
}

interface Span {
  start: number
  end: number
}

export function toAstronomical(cliopatriaYear: number): number {
  return cliopatriaYear < 0 ? fromHistorical(-cliopatriaYear, 'bc') : cliopatriaYear
}

function windowed(rows: Row[], { from = -Infinity, to = Infinity }: { from?: number; to?: number }): Row[] {
  return rows.map((row) => ({ ...row, from: Math.max(row.from, from), to: Math.min(row.to, to) })).filter((row) => row.from <= row.to)
}

function withoutOverlaps(rows: Row[]): Row[] {
  const sorted = rows.toSorted((a, b) => a.from - b.from)
  return sorted
    .map((row, index) => ({ ...row, to: Math.min(row.to, (sorted[index + 1]?.from ?? Infinity) - 1) }))
    .filter((row) => row.from <= row.to)
}

function distance(row: Row, span: Span): number {
  return Math.max(span.start - row.to, row.from - span.end)
}

function alignedToSpan(rows: Row[], span: Span): Row[] {
  const inside = rows
    .filter((row) => row.to >= span.start && row.from <= span.end)
    .map((row) => ({ ...row, from: Math.max(row.from, span.start), to: Math.min(row.to, span.end) }))
  const first = inside[0]
  const last = inside.at(-1)
  if (!first || !last) {
    const nearest = rows.filter((row) => distance(row, span) <= ALIGN_YEARS).toSorted((a, b) => distance(a, span) - distance(b, span))[0]
    return nearest ? [{ ...nearest, from: span.start, to: span.end }] : []
  }
  if (first.from - span.start <= ALIGN_YEARS) first.from = span.start
  if (span.end - last.to <= ALIGN_YEARS) last.to = span.end
  return inside
}

function splitByMerges(track: TrackId, row: Row, merges: Row[]): Plan[] {
  const overlapping = merges.filter((merge) => merge.to >= row.from && merge.from <= row.to)
  const cuts = [...new Set([row.from, ...overlapping.flatMap((merge) => [merge.from, merge.to + 1])])]
    .filter((year) => year >= row.from && year <= row.to)
    .sort((a, b) => a - b)
  return cuts.map((from, index) => ({
    track,
    polity: row.polity,
    from,
    to: (cuts[index + 1] ?? row.to + 1) - 1,
    rows: [row, ...overlapping.filter((merge) => merge.from <= from && merge.to >= from)],
  }))
}

export function withBridgedGaps(rows: Row[]): Row[] {
  const result: Row[] = []
  for (const row of rows) {
    const previous = result.at(-1)
    const bridged =
      previous &&
      previous.polity === row.polity &&
      row.from - previous.to - 1 <= BRIDGE_YEARS &&
      JSON.stringify(previous.geometry) === JSON.stringify(row.geometry)
    if (bridged) previous.to = row.to
    else result.push({ ...row })
  }
  return result
}

export function planTrack(track: TrackId, spans: Span[], primary: Row[], merges: Row[]): Plan[] {
  const resolved = withoutOverlaps(primary)
  return spans
    .map((span) => alignedToSpan(resolved, span))
    .flatMap(withBridgedGaps)
    .flatMap((row) => splitByMerges(track, row, merges))
}

export function planSlices(rows: Row[]): Plan[] {
  const plan = (track: Track) => {
    const sourcesOf = (merge: boolean) =>
      SOURCES.filter((source) => source.track === track.id && (source.merge ?? false) === merge).flatMap((source) =>
        windowed(
          rows.filter((row) => row.polity === source.polity),
          source,
        ),
      )
    return planTrack(track.id, track.spans, sourcesOf(false), sourcesOf(true))
  }
  return tracks.flatMap(plan)
}

const round = (value: number) => Math.round(value * 100) / 100

function ringArea(ring: LonLat[]): number {
  let sum = 0
  for (let index = 0; index + 1 < ring.length; index++) {
    const [x0, y0] = ring[index] ?? [0, 0]
    const [x1, y1] = ring[index + 1] ?? [0, 0]
    sum += x0 * y1 - x1 * y0
  }
  return sum / 2
}

export function cleanRing(ring: number[][]): LonLat[] | null {
  const points: LonLat[] = []
  for (const [lon = 0, lat = 0] of ring) {
    const point: LonLat = [round(lon), round(lat)]
    const last = points.at(-1)
    if (!last || last[0] !== point[0] || last[1] !== point[1]) points.push(point)
  }
  const first = points[0]
  const last = points.at(-1)
  if (first && last && (first[0] !== last[0] || first[1] !== last[1])) points.push([first[0], first[1]])
  return points.length >= 4 && ringArea(points) !== 0 ? points : null
}

function cleanPolygons(geometry: Geometry): LonLat[][][] {
  const polygons = geometry.type === 'Polygon' ? [geometry.coordinates] : geometry.coordinates
  return polygons.flatMap(([outer = [], ...holes]) => {
    const shell = cleanRing(outer)
    return shell ? [[shell, ...holes.map(cleanRing).filter((hole) => hole !== null)]] : []
  })
}

function boundsOf(polygons: LonLat[][][]): Slice['bounds'] {
  const points = polygons.flatMap(([outer = []]) => outer)
  const lons = points.map(([lon]) => lon)
  const lats = points.map(([, lat]) => lat)
  return [Math.min(...lons), Math.min(...lats), Math.max(...lons), Math.max(...lats)]
}

export function mergedRuns(slices: Slice[]): Slice[] {
  const result: Slice[] = []
  for (const slice of slices) {
    const previous = result.at(-1)
    const continues =
      previous &&
      previous.track === slice.track &&
      previous.polity === slice.polity &&
      previous.to + 1 === slice.from &&
      JSON.stringify(previous.polygons) === JSON.stringify(slice.polygons)
    if (continues) previous.to = slice.to
    else result.push({ ...slice })
  }
  return result
}

export function uncoveredYears(slices: Pick<Slice, 'track' | 'from' | 'to'>[], trackIds: TrackId[], start: number, end: number): number[] {
  const relevant = slices.filter((slice) => trackIds.includes(slice.track))
  const years: number[] = []
  for (let year = start; year <= end; year++) {
    if (!relevant.some((slice) => slice.from <= year && slice.to >= year)) years.push(year)
  }
  return years
}

async function cachedArchive(): Promise<string> {
  const file = `${CACHE}/cliopatria.geojson.zip`
  if (!existsSync(file)) {
    console.log(`Downloading ${ARCHIVE_URL}`)
    const response = await fetch(ARCHIVE_URL)
    if (!response.ok) throw new Error(`${ARCHIVE_URL} answered ${response.status}`)
    mkdirSync(CACHE, { recursive: true })
    writeFileSync(file, new Uint8Array(await response.arrayBuffer()))
  }
  const digest = createHash('sha256').update(readFileSync(file)).digest('hex')
  if (digest !== ARCHIVE_SHA256) throw new Error(`${file} has SHA-256 ${digest}, expected ${ARCHIVE_SHA256}`)
  return file
}

async function mapshaperOutput(commands: string, input?: Record<string, string>): Promise<unknown> {
  const output = await mapshaper.applyCommands(`${commands} -o result.json format=geojson geojson-type=FeatureCollection`, input)
  const result = output['result.json']
  return result === undefined ? null : JSON.parse(typeof result === 'string' ? result : new TextDecoder().decode(result))
}

async function readRows(archive: string): Promise<Row[]> {
  const polities = [...new Set(SOURCES.map((source) => source.polity))]
  const extract = await mapshaperOutput(`-i ${archive} -filter '${JSON.stringify(polities)}.includes(Name)'`)
  const { features } = cliopatriaSchema.parse(extract)
  const missing = polities.filter((polity) => !features.some((feature) => feature.properties.Name === polity))
  if (missing.length > 0) throw new Error(`Cliopatria ${RELEASE} has no rows for ${missing.join(', ')}`)
  return features
    .filter((feature) => feature.properties.Type === 'POLITY')
    .map(({ properties, geometry }) => ({
      polity: properties.Name,
      from: toAstronomical(properties.FromYear),
      to: toAstronomical(properties.ToYear),
      geometry,
    }))
}

async function simplified(plan: Plan): Promise<Geometry[]> {
  const { west, south, east, north } = MAP_BOUNDS
  const collection = JSON.stringify({
    type: 'FeatureCollection',
    features: plan.rows.map((row) => ({ type: 'Feature', properties: { track: plan.track }, geometry: row.geometry })),
  })
  const output = await mapshaperOutput(
    `-i plan.json -clip bbox=${west},${south},${east},${north} -dissolve track -filter-islands min-area=${MIN_ISLAND} -explode -simplify visvalingam variable interval='this.area < ${SMALL_RING_AREA} ? ${SMALL_RING_METERS} : ${SIMPLIFY_METERS}' keep-shapes`,
    { 'plan.json': collection },
  )
  return output === null ? [] : simplifiedSchema.parse(output).features.flatMap((feature) => feature.geometry ?? [])
}

async function labelPoint(polygons: LonLat[][][]): Promise<LonLat> {
  const shape = JSON.stringify({
    type: 'FeatureCollection',
    features: [{ type: 'Feature', properties: {}, geometry: { type: 'MultiPolygon', coordinates: polygons } }],
  })
  const [lon = 0, lat = 0] = pointSchema.parse(await mapshaperOutput('-i shape.json -points inner', { 'shape.json': shape })).features[0]!.geometry.coordinates
  return [round(lon), round(lat)]
}

function serialize(slices: Slice[]): string {
  return `{"attribution":${JSON.stringify(ATTRIBUTION)},"slices":[\n${slices.map((slice) => JSON.stringify(slice)).join(',\n')}\n]}\n`
}

async function main() {
  const plans = planSlices(await readRows(await cachedArchive()))
  const geometries: Geometry[][] = []
  for (const plan of plans) geometries.push(await simplified(plan))
  const drafts: Slice[] = []
  for (const [index, plan] of plans.entries()) {
    const polygons = (geometries[index] ?? []).flatMap(cleanPolygons)
    if (polygons.length === 0) {
      console.warn(`No geometry left for ${plan.track} ${plan.polity} from ${plan.from} to ${plan.to}`)
      continue
    }
    drafts.push({ track: plan.track, polity: plan.polity, from: plan.from, to: plan.to, bounds: boundsOf(polygons), label: await labelPoint(polygons), polygons })
  }
  const slices = mergedRuns(drafts)
  const text = serialize(slices)
  mkdirSync(dirname(TERRITORIES_FILE), { recursive: true })
  writeFileSync(TERRITORIES_FILE, text)
  const size = Buffer.byteLength(text)
  for (const id of TRACK_IDS) {
    const own = slices.filter((slice) => slice.track === id)
    console.log(`${id}: ${own.length} slices, ${[...new Set(own.map((slice) => slice.polity))].join(', ')}`)
  }
  for (const track of tracks) {
    const uncovered = track.spans.flatMap((span) => uncoveredYears(slices, [track.id], span.start, span.end))
    if (uncovered.length > 0) console.log(`${track.id}: ${uncovered.length} years without territory, from ${uncovered[0]} to ${uncovered.at(-1)}`)
  }
  console.log(`${TERRITORIES_FILE}: ${slices.length} slices, ${size} bytes${size > SIZE_TARGET ? `, above the ${SIZE_TARGET} byte target` : ''}`)
}

if (import.meta.main) await main()
