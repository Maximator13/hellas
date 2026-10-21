import { existsSync, readFileSync } from 'node:fs'
import { describe, expect, it } from 'vitest'
import { tracks } from '../../src/data/tracks.ts'
import { MAP_BOUNDS } from '../../src/map/geo.ts'
import {
  HAND_DRAWN_FILE,
  SIZE_TARGET,
  TERRITORIES_FILE,
  byTrackThenStart,
  handDrawnSchema,
  planHandDrawn,
  cleanRing,
  mergedRuns,
  planTrack,
  territoriesSchema,
  toAstronomical,
  uncoveredYears,
  withBridgedGaps,
} from './territories.ts'
import type { Row, Slice } from './territories.ts'

const text = readFileSync(TERRITORIES_FILE, 'utf8')
const { attribution, slices } = territoriesSchema.parse(JSON.parse(text))
const square: Row['geometry'] = { type: 'Polygon', coordinates: [[[0, 0], [1, 0], [1, 1], [0, 0]]] }
const row = (polity: string, from: number, to: number): Row => ({ polity, from, to, geometry: square })

describe('Cliopatria years', () => {
  it('reads negative years as historical BCE years and the filler year 0 as 1 BCE', () => {
    expect(toAstronomical(-753)).toBe(-752)
    expect(toAstronomical(-31)).toBe(-30)
    expect(toAstronomical(-1)).toBe(0)
    expect(toAstronomical(0)).toBe(0)
    expect(toAstronomical(1)).toBe(1)
    expect(toAstronomical(1453)).toBe(1453)
  })
})

describe('slice planning', () => {
  it('lets the later row win from its start and stretches the edges to the track span', () => {
    const plans = planTrack(
      'macedoine',
      [{ start: -649, end: -167 }],
      [row('Argead', -646, -400), row('Argead', -399, -380), row('Antigonid', -399, -170)],
      [],
    )
    expect(plans.map(({ polity, from, to }) => [polity, from, to])).toEqual([
      ['Argead', -649, -400],
      ['Antigonid', -399, -167],
    ])
  })

  it('clamps rows to every span and leaves edges far from the span alone', () => {
    const plans = planTrack(
      'athenes',
      [
        { start: -799, end: -500 },
        { start: -400, end: -85 },
      ],
      [row('Athens', -780, -499), row('Athens', -498, -480), row('Athens', -380, -60)],
      [],
    )
    expect(plans.map(({ from, to }) => [from, to])).toEqual([
      [-780, -500],
      [-380, -85],
    ])
  })

  it('moves the nearest row into a span that no row reaches', () => {
    const latest = { ...row('Thebans', -340, -338), geometry: { ...square } }
    const plans = planTrack('thebes', [{ start: -337, end: -334 }], [row('Thebans', -350, -345), latest], [])
    expect(plans.map(({ from, to }) => [from, to])).toEqual([[-337, -334]])
    expect(plans[0]?.rows[0]?.geometry).toBe(latest.geometry)
  })

  it('bridges gaps of at most ten years between rows of one polity with identical geometry', () => {
    const larger: Row = { ...row('Rhodes', -170, -165), geometry: { type: 'Polygon', coordinates: [[[0, 0], [2, 0], [2, 2], [0, 0]]] } }
    const rows = [row('Pergamon', -280, -250), row('Pergamon', -244, -230), row('Pergamon', -219, -200), row('Pergamon', -188, -180), row('Rhodes', -178, -175), larger]
    expect(withBridgedGaps(rows).map(({ polity, from, to }) => [polity, from, to])).toEqual([
      ['Pergamon', -280, -200],
      ['Pergamon', -188, -180],
      ['Rhodes', -178, -175],
      ['Rhodes', -170, -165],
    ])
    expect(rows[0]?.to).toBe(-250)
  })

  it('bridges such gaps on every track', () => {
    const rows = [row('Seleucid Empire', -311, -200), row('Seleucid Empire', -194, -62)]
    expect(planTrack('seleucides', [{ start: -311, end: -62 }], rows, []).map(({ from, to }) => [from, to])).toEqual([[-311, -62]])
  })

  it('splits a slice where merged territory joins it', () => {
    const plans = planTrack('alexandre', [{ start: -335, end: -300 }], [row('Macedonian Empire', -335, -300)], [row('Ptolemaic Kingdom', -330, -323)])
    expect(plans.map(({ from, to, rows }) => [from, to, rows.map((part) => part.polity)])).toEqual([
      [-335, -331, ['Macedonian Empire']],
      [-330, -323, ['Macedonian Empire', 'Ptolemaic Kingdom']],
      [-322, -300, ['Macedonian Empire']],
    ])
  })
})

describe('hand-drawn territories', () => {
  it('unions the drawn shapes active together and cuts where one starts or ends', () => {
    const plans = planHandDrawn('athenes', [row('Attique', -799, -85), row('Empire athénien', -477, -404)])
    expect(plans.map(({ polity, from, to }) => [polity, from, to])).toEqual([
      ['Attique', -799, -478],
      ['Attique et Empire athénien', -477, -404],
      ['Attique', -403, -85],
    ])
  })

  it('keeps every drawn shape inside its track span with sources', () => {
    if (!existsSync(HAND_DRAWN_FILE)) return
    const { features } = handDrawnSchema.parse(JSON.parse(readFileSync(HAND_DRAWN_FILE, 'utf8')))
    for (const { properties } of features) {
      const track = tracks.find((candidate) => candidate.id === properties.track)
      expect(track?.spans.some((span) => span.start <= properties.from && properties.to <= span.end), `${properties.track} ${properties.from}`).toBe(true)
    }
  })
})

describe('geometry cleaning', () => {
  it('rounds to two decimals, drops repeated points and closes the ring', () => {
    expect(cleanRing([[1.234, 2.001], [3.001, 2.004], [3.004, 4], [1.2, 4.001]])).toEqual([
      [1.23, 2],
      [3, 2],
      [3, 4],
      [1.2, 4],
      [1.23, 2],
    ])
  })

  it('rejects rings that collapse when rounded', () => {
    expect(cleanRing([[1, 1], [1.001, 1.001], [1.002, 1], [1, 1]])).toBeNull()
    expect(cleanRing([[0, 0], [1, 1], [2, 2], [0, 0]])).toBeNull()
  })

  it('joins consecutive identical slices of the same polity', () => {
    const base: Slice = { track: 'macedoine', polity: 'Argead', from: -649, to: -600, bounds: [0, 0, 1, 1], label: [0.5, 0.5], polygons: [] }
    expect(mergedRuns([base, { ...base, from: -599, to: -400 }, { ...base, polity: 'Antigonid', from: -399, to: -380 }])).toEqual([
      { ...base, to: -400 },
      { ...base, polity: 'Antigonid', from: -399, to: -380 },
    ])
  })
})

describe('territories file', () => {
  it('credits Cliopatria under CC BY 4.0 and states the changes', () => {
    for (const part of ['J. S. Bennett, E. Mutch, A. Tollefson et al.', 'v0.2.1', 'https://github.com/Seshat-Global-History-Databank/cliopatria', 'CC BY 4.0', 'modifié']) {
      expect(attribution).toContain(part)
    }
  })

  it('stays within the size target', () => {
    expect(Buffer.byteLength(text)).toBeLessThanOrEqual(SIZE_TARGET)
  })

  it('keeps every slice inside the spans of a known track', () => {
    for (const slice of slices) {
      const track = tracks.find((candidate) => candidate.id === slice.track)
      expect(track, slice.track).toBeDefined()
      expect(slice.from).toBeLessThanOrEqual(slice.to)
      expect(track?.spans.some((span) => span.start <= slice.from && slice.to <= span.end), `${slice.track} ${slice.from}`).toBe(true)
    }
  })

  it('sorts slices by track then start and never overlaps two slices of one polity', () => {
    slices.forEach((slice, index) => {
      const previous = slices[index - 1]
      if (previous) expect(byTrackThenStart(previous, slice), `${slice.track} ${slice.from}`).toBeLessThanOrEqual(0)
      const twins = slices.filter((other) => other !== slice && other.track === slice.track && other.polity === slice.polity)
      expect(twins.some((other) => other.from <= slice.to && slice.from <= other.to), `${slice.track} ${slice.polity} ${slice.from}`).toBe(false)
    })
  })

  it('draws the Greek world and the Persian empire over their whole span', () => {
    for (const track of tracks.filter((candidate) => ['monde-grec', 'perse'].includes(candidate.id))) {
      const uncovered = track.spans.flatMap((span) => uncoveredYears(slices, [track.id], span.start, span.end))
      expect(uncovered, track.id).toEqual([])
    }
  })

  it('stores closed rings of at least four points inside the map bounds', () => {
    for (const slice of slices) {
      expect(slice.polygons.length, `${slice.track} ${slice.from}`).toBeGreaterThan(0)
      const [west, south, east, north] = slice.bounds
      for (const ring of slice.polygons.flat()) {
        expect(ring.length).toBeGreaterThanOrEqual(4)
        expect(ring.at(-1)).toEqual(ring[0])
        for (const [lon, lat] of ring) {
          expect(lon >= MAP_BOUNDS.west && lon <= MAP_BOUNDS.east && lat >= MAP_BOUNDS.south && lat <= MAP_BOUNDS.north).toBe(true)
          expect(lon >= west && lon <= east && lat >= south && lat <= north).toBe(true)
        }
      }
      expect(slice.label[0] >= west && slice.label[0] <= east && slice.label[1] >= south && slice.label[1] <= north).toBe(true)
    }
  })
})
