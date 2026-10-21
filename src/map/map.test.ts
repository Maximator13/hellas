import { describe, expect, it } from 'vitest'
import { MAX_DISTANCE, MIN_DISTANCE, approach, approachGoal, fitDistance, frameAt, goalForBounds, goalForPlace } from './camera.ts'
import { activeSlices, sliceKey, type TerritorySlice } from './territories.ts'

const slice = (track: TerritorySlice['track'], from: number, to: number, bounds: TerritorySlice['bounds']): TerritorySlice => ({
  track,
  polity: track,
  from,
  to,
  bounds,
  label: [(bounds[0] + bounds[2]) / 2, (bounds[1] + bounds[3]) / 2],
  polygons: [],
})

const persia = slice('perse', -549, -330, [25, 22, 75, 45])
const athens = slice('athenes', -365, -338, [22, 36, 28, 40])
const thebes = slice('thebes', -350, -338, [22, 37, 24, 39])

describe('territory slices', () => {
  it('selects the slices active at a year, inclusive', () => {
    expect(activeSlices([persia, athens, thebes], -330)).toEqual([persia])
    expect(activeSlices([persia, athens, thebes], -345)).toEqual([persia, athens, thebes])
    expect(activeSlices([persia, athens, thebes], -100)).toEqual([])
  })

  it('identifies a set of slices so transitions start only on change', () => {
    expect(sliceKey([athens, thebes])).toBe('athenes:-365|thebes:-350')
    expect(sliceKey(activeSlices([persia], -400))).toBe(sliceKey(activeSlices([persia], -390)))
  })
})

describe('camera frames', () => {
  it('frames the Aegean, then the colonies, then Alexander and the kingdoms', () => {
    expect(frameAt(-1500)).toEqual([19, 34.5, 30.5, 42])
    expect(frameAt(-650)[0]).toBe(-7)
    expect(frameAt(-480)).toEqual([19, 34.5, 30.5, 42])
    expect(frameAt(-330)[2]).toBe(78)
    expect(frameAt(-100)[2]).toBe(52)
  })
})

describe('camera goals', () => {
  it('pulls back as the territory grows', () => {
    const small = goalForBounds(thebes.bounds, 40, 16 / 9)
    const large = goalForBounds(persia.bounds, 40, 16 / 9)
    expect(large.distance).toBeGreaterThan(small.distance)
  })

  it('keeps the distance within limits', () => {
    expect(fitDistance(0.1, 0.1, 40, 1.5)).toBe(MIN_DISTANCE)
    expect(fitDistance(500, 500, 40, 1.5)).toBe(MAX_DISTANCE)
  })

  it('centres a place close up', () => {
    const athens = goalForPlace(23.73, 37.97)
    expect(athens.distance).toBeLessThan(10)
  })

  it('approaches the goal smoothly and reaches it immediately without a time constant', () => {
    expect(approach(0, 10, 0.5, 0)).toBe(10)
    const step = approach(0, 10, 0.5, 0.5)
    expect(step).toBeGreaterThan(5)
    expect(step).toBeLessThan(10)
    const goal = approachGoal({ x: 0, z: 0, distance: 4 }, { x: 10, z: 10, distance: 16 }, 10, 0.5)
    expect(goal.x).toBeCloseTo(10)
    expect(goal.distance).toBeCloseTo(16)
  })
})
