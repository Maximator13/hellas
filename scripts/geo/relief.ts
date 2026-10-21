import { existsSync, mkdirSync, readFileSync, statSync, writeFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fromArrayBuffer } from 'geotiff'
import sharp from 'sharp'
import { z } from 'zod'
import { MAP_BOUNDS, RELIEF_GRID, RELIEF_TILE_COLUMNS, RELIEF_TILES, encodeElevation, type ReliefTile } from '../../src/map/geo.ts'

const CACHE = '.cache/geo'
export const reliefFile = (tile: ReliefTile) => `public/geo/relief-${tile}.webp`
export const SIZE_TARGET = 3_000_000
const SHORE_METERS = 2
const ETOPO_CELLS_PER_DEGREE = 120
const ETOPO_RASTER = 'ETOPO_2022_v1_30s_surface'
const ETOPO_CACHE = `etopo-2022-30s-surface-${MAP_BOUNDS.west}-${MAP_BOUNDS.south}-${MAP_BOUNDS.east}-${MAP_BOUNDS.north}.tif`
const ETOPO_WIDTH = (MAP_BOUNDS.east - MAP_BOUNDS.west) * ETOPO_CELLS_PER_DEGREE
const ETOPO_HEIGHT = (MAP_BOUNDS.north - MAP_BOUNDS.south) * ETOPO_CELLS_PER_DEGREE

const ETOPO_URL = `https://gis.ngdc.noaa.gov/arcgis/rest/services/DEM_mosaics/DEM_all/ImageServer/exportImage?${new URLSearchParams({
  bbox: `${MAP_BOUNDS.west},${MAP_BOUNDS.south},${MAP_BOUNDS.east},${MAP_BOUNDS.north}`,
  bboxSR: '4326',
  imageSR: '4326',
  size: `${ETOPO_WIDTH},${ETOPO_HEIGHT}`,
  format: 'tiff',
  pixelType: 'F32',
  interpolation: 'RSP_NearestNeighbor',
  noData: '-99999',
  mosaicRule: JSON.stringify({ mosaicMethod: 'esriMosaicNone', where: `Name='${ETOPO_RASTER}'` }),
  f: 'image',
})}`

const NATURAL_EARTH = 'https://raw.githubusercontent.com/nvkelso/natural-earth-vector/v5.1.2/geojson'

const position = z.tuple([z.number(), z.number()]).rest(z.number())
const ring = z.array(position)
const geometry = z.discriminatedUnion('type', [
  z.object({ type: z.literal('Polygon'), coordinates: z.array(ring) }),
  z.object({ type: z.literal('MultiPolygon'), coordinates: z.array(z.array(ring)) }),
])
const featureCollection = z.object({
  features: z.array(z.object({ properties: z.object({ featurecla: z.string().nullable() }), geometry })),
})

type Ring = z.infer<typeof ring>
type FeatureCollection = z.infer<typeof featureCollection>

async function cachedSource<T>(url: string, name: string, parse: (bytes: Uint8Array<ArrayBuffer>) => Promise<T> | T): Promise<T> {
  const file = join(CACHE, name)
  if (existsSync(file)) return parse(new Uint8Array(readFileSync(file)))
  console.log(`Downloading ${url}`)
  const response = await fetch(url)
  if (!response.ok) throw new Error(`${url} answered ${response.status}`)
  const bytes = new Uint8Array(await response.arrayBuffer())
  const parsed = await parse(bytes)
  mkdirSync(CACHE, { recursive: true })
  writeFileSync(file, bytes)
  return parsed
}

async function parseEtopo(bytes: Uint8Array<ArrayBuffer>): Promise<Float32Array> {
  const image = await (await fromArrayBuffer(bytes.buffer)).getImage()
  const box = image.getBoundingBox()
  const expectedBox = [MAP_BOUNDS.west, MAP_BOUNDS.south, MAP_BOUNDS.east, MAP_BOUNDS.north]
  if (image.getWidth() !== ETOPO_WIDTH || image.getHeight() !== ETOPO_HEIGHT || box.some((value, index) => Math.abs(value - (expectedBox[index] ?? NaN)) > 1e-6)) {
    throw new Error(`Unexpected ETOPO grid ${image.getWidth()}x${image.getHeight()} over ${box.join(',')}`)
  }
  const values = await image.readRasters({ interleave: true })
  if (!(values instanceof Float32Array)) throw new Error('ETOPO raster is not 32-bit float')
  if (values.some((value) => !Number.isFinite(value) || value < -11000 || value > 9000)) throw new Error('ETOPO raster holds no-data cells')
  return values
}

function parseGeoJson(bytes: Uint8Array): FeatureCollection {
  return featureCollection.parse(JSON.parse(new TextDecoder().decode(bytes)))
}

function ringsOf(collection: FeatureCollection, keep: (featurecla: string | null) => boolean): Ring[] {
  return collection.features
    .filter((feature) => keep(feature.properties.featurecla))
    .flatMap(({ geometry }) => (geometry.type === 'Polygon' ? geometry.coordinates : geometry.coordinates.flat()))
}

function rasterize(rings: Ring[], width: number, height: number): Uint8Array {
  const { west, east, south, north } = MAP_BOUNDS
  const crossings: number[][] = Array.from({ length: height }, () => [])
  const column = (lon: number) => ((lon - west) / (east - west)) * width - 0.5
  const row = (lat: number) => ((north - lat) / (north - south)) * height - 0.5
  for (const points of rings) {
    points.forEach((start, index) => {
      const end = points[(index + 1) % points.length] ?? start
      const [x0, y0, x1, y1] = [column(start[0]), row(start[1]), column(end[0]), row(end[1])]
      if (y0 === y1) return
      const last = Math.min(height - 1, Math.ceil(Math.max(y0, y1)) - 1)
      for (let y = Math.max(0, Math.ceil(Math.min(y0, y1))); y <= last; y++) {
        crossings[y]?.push(x0 + ((y - y0) * (x1 - x0)) / (y1 - y0))
      }
    })
  }
  const mask = new Uint8Array(width * height)
  crossings.forEach((xs, y) => {
    xs.sort((a, b) => a - b)
    for (let pair = 0; pair + 1 < xs.length; pair += 2) {
      const from = Math.max(0, Math.ceil(xs[pair] ?? 0))
      const to = Math.min(width, Math.ceil(xs[pair + 1] ?? 0))
      if (to > from) mask.fill(1, y * width + from, y * width + to)
    }
  })
  return mask
}

function boxWeights(sourceLength: number, targetLength: number): { start: number; weights: number[] }[] {
  const scale = sourceLength / targetLength
  return Array.from({ length: targetLength }, (_, index) => {
    const from = index * scale
    const to = Math.min(sourceLength, from + scale)
    const start = Math.floor(from)
    const weights: number[] = []
    for (let source = start; source < to; source++) weights.push((Math.min(to, source + 1) - Math.max(from, source)) / scale)
    return { start, weights }
  })
}

function resample(values: ArrayLike<number>, width: number, height: number, targetWidth: number, targetHeight: number): Float32Array {
  const columns = boxWeights(width, targetWidth)
  const rows = boxWeights(height, targetHeight)
  const horizontal = new Float32Array(height * targetWidth)
  for (let y = 0; y < height; y++) {
    columns.forEach(({ start, weights }, x) => {
      horizontal[y * targetWidth + x] = weights.reduce((sum, weight, k) => sum + weight * (values[y * width + start + k] ?? 0), 0)
    })
  }
  const result = new Float32Array(targetWidth * targetHeight)
  rows.forEach(({ start, weights }, y) => {
    for (let x = 0; x < targetWidth; x++) {
      result[y * targetWidth + x] = weights.reduce((sum, weight, k) => sum + weight * (horizontal[(start + k) * targetWidth + x] ?? 0), 0)
    }
  })
  return result
}

function tileOf(bytes: Uint8Array, width: number, height: number, tile: number): Uint8Array {
  const offset = tile * (RELIEF_TILE_COLUMNS - 1)
  const result = new Uint8Array(RELIEF_TILE_COLUMNS * height)
  for (let row = 0; row < height; row++) {
    result.set(bytes.subarray(row * width + offset, row * width + offset + RELIEF_TILE_COLUMNS), row * RELIEF_TILE_COLUMNS)
  }
  return result
}

async function main() {
  const { columns: width, rows: height } = RELIEF_GRID
  const etopo = await cachedSource(ETOPO_URL, ETOPO_CACHE, parseEtopo)
  const land = await cachedSource(`${NATURAL_EARTH}/ne_10m_land.geojson`, 'ne_10m_land.geojson', parseGeoJson)
  const lakes = await cachedSource(`${NATURAL_EARTH}/ne_10m_lakes.geojson`, 'ne_10m_lakes.geojson', parseGeoJson)
  const elevation = resample(etopo, ETOPO_WIDTH, ETOPO_HEIGHT, width, height)
  const landMask = rasterize(ringsOf(land, () => true), width, height)
  const lakeMask = rasterize(ringsOf(lakes, (featurecla) => featurecla !== 'Reservoir'), width, height)
  const bytes = new Uint8Array(width * height)
  bytes.forEach((_, index) => {
    const meters = elevation[index] ?? 0
    const water = landMask[index] === 0 || lakeMask[index] === 1
    bytes[index] = encodeElevation(water ? Math.min(meters, -SHORE_METERS) : Math.max(meters, SHORE_METERS))
  })
  for (const [index, tile] of RELIEF_TILES.entries()) {
    const file = reliefFile(tile)
    mkdirSync(dirname(file), { recursive: true })
    await sharp(tileOf(bytes, width, height, index), { raw: { width: RELIEF_TILE_COLUMNS, height, channels: 1 } })
      .webp({ lossless: true, effort: 6 })
      .toFile(file)
    const size = statSync(file).size
    console.log(`${file}: ${RELIEF_TILE_COLUMNS}x${height}, ${size} bytes${size > SIZE_TARGET ? `, above the ${SIZE_TARGET} byte target` : ''}`)
  }
}

if (import.meta.main) await main()
