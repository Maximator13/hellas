import type { TrackId } from '../data/schema.ts'

export type Ring = [number, number][]
export type Polygon = Ring[]
export type Bounds = [west: number, south: number, east: number, north: number]

export interface TerritorySlice {
  track: TrackId
  polity: string
  from: number
  to: number
  bounds: Bounds
  label: [number, number]
  polygons: Polygon[]
}

export interface TerritoryData {
  attribution: string
  slices: TerritorySlice[]
}

export function activeSlices(slices: TerritorySlice[], year: number): TerritorySlice[] {
  const rounded = Math.round(year)
  return slices.filter((slice) => rounded >= slice.from && rounded <= slice.to)
}

export function sliceKey(slices: TerritorySlice[]): string {
  return slices.map((slice) => `${slice.track}:${slice.from}`).join('|')
}
