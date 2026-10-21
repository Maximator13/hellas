import { RELIEF_GRID, RELIEF_TILE_COLUMNS, decodeElevation, gridCell, tileColumn } from './geo.ts'

export type HeightSampler = (lon: number, lat: number) => number

export function createHeightSampler(tiles: (Uint8Array | null)[], landScale: number): HeightSampler {
  return (lon, lat) => {
    const { column, row } = gridCell(lon, lat)
    if (column < 0 || row < 0 || column >= RELIEF_GRID.columns || row >= RELIEF_GRID.rows) return 0
    const local = tileColumn(column)
    const byte = tiles[local.tile]?.[row * RELIEF_TILE_COLUMNS + local.column]
    return byte === undefined ? 0 : Math.max(0, decodeElevation(byte)) * landScale
  }
}
