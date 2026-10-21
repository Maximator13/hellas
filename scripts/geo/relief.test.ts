import { statSync } from 'node:fs'
import sharp from 'sharp'
import { beforeAll, describe, expect, it } from 'vitest'
import { RELIEF_GRID, RELIEF_TILE_COLUMNS, RELIEF_TILES, decodeElevation, gridCell, tileColumn } from '../../src/map/geo.ts'
import { SIZE_TARGET, reliefFile } from './relief.ts'

const tiles: Uint8Array[] = []

function byteAt(lon: number, lat: number): number {
  const { column, row } = gridCell(lon, lat)
  const local = tileColumn(column)
  return tiles[local.tile]?.[row * RELIEF_TILE_COLUMNS + local.column] ?? NaN
}

function metersAt(lon: number, lat: number): number {
  return decodeElevation(byteAt(lon, lat))
}

describe('relief tiles', () => {
  beforeAll(async () => {
    for (const tile of RELIEF_TILES) {
      const { data, info } = await sharp(reliefFile(tile)).extractChannel(0).raw().toBuffer({ resolveWithObject: true })
      expect([info.width, info.height, info.channels]).toEqual([RELIEF_TILE_COLUMNS, RELIEF_GRID.rows, 1])
      tiles.push(new Uint8Array(data))
    }
  })

  it('stays under the weight target and stays within the mobile texture limit', () => {
    expect(RELIEF_TILE_COLUMNS).toBeLessThanOrEqual(4096)
    expect(RELIEF_GRID.rows).toBeLessThanOrEqual(4096)
    for (const tile of RELIEF_TILES) expect(statSync(reliefFile(tile)).size).toBeLessThanOrEqual(SIZE_TARGET)
  })

  it('shares the seam column so the two tiles join without a step', () => {
    for (let row = 0; row < RELIEF_GRID.rows; row += 97) {
      expect(tiles[0]?.[row * RELIEF_TILE_COLUMNS + RELIEF_TILE_COLUMNS - 1]).toBe(tiles[1]?.[row * RELIEF_TILE_COLUMNS])
    }
  })

  it('keeps a clear gap between water and land around sea level', () => {
    expect(tiles.some((pixels) => pixels.some((byte) => byte >= 126 && byte <= 129))).toBe(false)
  })

  it('puts land, sea and summits where they belong', () => {
    expect(metersAt(23.73, 37.97)).toBeGreaterThan(0)
    expect(metersAt(23.73, 37.97)).toBeLessThan(400)
    expect(metersAt(25, 36)).toBeLessThan(-500)
    expect(metersAt(22.36, 40.09)).toBeGreaterThan(2000)
    expect(metersAt(14.99, 37.75)).toBeGreaterThan(2200)
    expect(metersAt(31, 30.8)).toBeGreaterThan(0)
    expect(metersAt(72, 35.9)).toBeGreaterThan(3000)
    expect(metersAt(65, 23.5)).toBeLessThan(0)
  })

  it('reads land below sea level as land and inland seas and lakes as water', () => {
    expect(metersAt(27, 29.6)).toBeGreaterThan(0)
    expect(metersAt(51, 42)).toBeLessThan(-200)
    expect(metersAt(42.9, 38.6)).toBeLessThan(0)
  })
})
