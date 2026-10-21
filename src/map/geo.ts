export const MAP_BOUNDS = { west: -7, east: 78, south: 22, north: 49 } as const

export const RELIEF_PIXELS_PER_DEGREE = 96

export const RELIEF_GRID = {
  columns: (MAP_BOUNDS.east - MAP_BOUNDS.west) * RELIEF_PIXELS_PER_DEGREE + 1,
  rows: (MAP_BOUNDS.north - MAP_BOUNDS.south) * RELIEF_PIXELS_PER_DEGREE + 1,
} as const

export const RELIEF_TILES = ['west', 'east'] as const

export type ReliefTile = (typeof RELIEF_TILES)[number]

export const RELIEF_TILE_COLUMNS = (RELIEF_GRID.columns - 1) / RELIEF_TILES.length + 1

export const RELIEF_ENCODING = { maxLand: 4800, maxDepth: 6000 } as const

export const PROJECTION_LATITUDE = (MAP_BOUNDS.south + MAP_BOUNDS.north) / 2

const LONGITUDE_SCALE = Math.cos((PROJECTION_LATITUDE * Math.PI) / 180)

export const MAP_SIZE = {
  width: (MAP_BOUNDS.east - MAP_BOUNDS.west) * LONGITUDE_SCALE,
  depth: MAP_BOUNDS.north - MAP_BOUNDS.south,
} as const

export interface MapPoint {
  x: number
  z: number
}

export function project(lon: number, lat: number): MapPoint {
  return {
    x: (lon - (MAP_BOUNDS.west + MAP_BOUNDS.east) / 2) * LONGITUDE_SCALE,
    z: -(lat - (MAP_BOUNDS.south + MAP_BOUNDS.north) / 2),
  }
}

export function toTextureUv(lon: number, lat: number): { u: number; v: number } {
  return {
    u: (lon - MAP_BOUNDS.west) / (MAP_BOUNDS.east - MAP_BOUNDS.west),
    v: (lat - MAP_BOUNDS.south) / (MAP_BOUNDS.north - MAP_BOUNDS.south),
  }
}

export function gridCell(lon: number, lat: number): { column: number; row: number } {
  return {
    column: Math.round(((lon - MAP_BOUNDS.west) / (MAP_BOUNDS.east - MAP_BOUNDS.west)) * (RELIEF_GRID.columns - 1)),
    row: Math.round(((MAP_BOUNDS.north - lat) / (MAP_BOUNDS.north - MAP_BOUNDS.south)) * (RELIEF_GRID.rows - 1)),
  }
}

export function tileColumn(column: number): { tile: number; column: number } {
  const step = RELIEF_TILE_COLUMNS - 1
  const tile = Math.min(RELIEF_TILES.length - 1, Math.floor(column / step))
  return { tile, column: column - tile * step }
}

export function encodeElevation(meters: number): number {
  const limit = meters >= 0 ? RELIEF_ENCODING.maxLand : RELIEF_ENCODING.maxDepth
  const scaled = Math.sqrt(Math.min(1, Math.abs(meters) / limit))
  return Math.round(127.5 + Math.sign(meters) * scaled * 127.5)
}

export function decodeElevation(byte: number): number {
  const signed = (byte - 127.5) / 127.5
  const limit = signed >= 0 ? RELIEF_ENCODING.maxLand : RELIEF_ENCODING.maxDepth
  return Math.sign(signed) * signed * signed * limit
}
