import { describe, expect, it } from 'vitest'
import { MAP_BOUNDS, MAP_SIZE, RELIEF_GRID, RELIEF_TILE_COLUMNS, decodeElevation, encodeElevation, gridCell, project, tileColumn, toTextureUv, unproject } from './geo.ts'

describe('projection', () => {
  it('centres the map on the middle of its bounds', () => {
    const center = project((MAP_BOUNDS.west + MAP_BOUNDS.east) / 2, (MAP_BOUNDS.south + MAP_BOUNDS.north) / 2)
    expect(center.x).toBeCloseTo(0)
    expect(center.z).toBeCloseTo(0)
  })

  it('puts north away from the viewer and east to the right', () => {
    const athens = project(23.73, 37.97)
    const babylon = project(44.42, 32.54)
    const pella = project(22.52, 40.76)
    expect(babylon.x).toBeGreaterThan(athens.x)
    expect(athens.z).toBeGreaterThan(pella.z)
  })

  it('spans the whole map size between the corners', () => {
    const southWest = project(MAP_BOUNDS.west, MAP_BOUNDS.south)
    const northEast = project(MAP_BOUNDS.east, MAP_BOUNDS.north)
    expect(northEast.x - southWest.x).toBeCloseTo(MAP_SIZE.width)
    expect(southWest.z - northEast.z).toBeCloseTo(MAP_SIZE.depth)
  })

  it('unprojects a projected point back to its coordinates', () => {
    const point = project(23.73, 37.97)
    const back = unproject(point.x, point.z)
    expect(back.lon).toBeCloseTo(23.73)
    expect(back.lat).toBeCloseTo(37.97)
  })

  it('maps the bounds to texture coordinates from 0 to 1', () => {
    expect(toTextureUv(MAP_BOUNDS.west, MAP_BOUNDS.south)).toEqual({ u: 0, v: 0 })
    expect(toTextureUv(MAP_BOUNDS.east, MAP_BOUNDS.north)).toEqual({ u: 1, v: 1 })
  })
})

describe('relief grid', () => {
  it('maps the corners to the first and last samples', () => {
    expect(gridCell(MAP_BOUNDS.west, MAP_BOUNDS.north)).toEqual({ column: 0, row: 0 })
    expect(gridCell(MAP_BOUNDS.east, MAP_BOUNDS.south)).toEqual({ column: RELIEF_GRID.columns - 1, row: RELIEF_GRID.rows - 1 })
  })

  it('splits columns into tiles that share the seam column', () => {
    const seam = RELIEF_TILE_COLUMNS - 1
    expect(tileColumn(seam - 1)).toEqual({ tile: 0, column: seam - 1 })
    expect(tileColumn(seam)).toEqual({ tile: 1, column: 0 })
    expect(tileColumn(RELIEF_GRID.columns - 1)).toEqual({ tile: 1, column: seam })
  })
})

describe('elevation encoding', () => {
  it('keeps sea level between the two middle bytes', () => {
    expect(encodeElevation(1)).toBe(129)
    expect(encodeElevation(-1)).toBe(126)
    expect(decodeElevation(128)).toBeGreaterThan(0)
    expect(decodeElevation(127)).toBeLessThan(0)
  })

  it('round trips mountains and deep sea within a few percent', () => {
    for (const meters of [4800, 2000, 300, -200, -3000, -6000]) {
      expect(Math.abs(decodeElevation(encodeElevation(meters)) - meters)).toBeLessThan(Math.abs(meters) * 0.05 + 40)
    }
  })

  it('clamps beyond the encoded range', () => {
    expect(encodeElevation(9000)).toBe(255)
    expect(encodeElevation(-11000)).toBe(0)
  })
})
