import { project } from './geo.ts'
import type { Bounds } from './territories.ts'

export interface CameraGoal {
  x: number
  z: number
  distance: number
}

export const CAMERA_FRAMES: { until: number; name: string; bounds: Bounds }[] = [
  { until: -800, name: 'egee', bounds: [19, 34.5, 30.5, 42] },
  { until: -550, name: 'mediterranee', bounds: [-7, 29, 42.5, 49] },
  { until: -336, name: 'egee', bounds: [19, 34.5, 30.5, 42] },
  { until: -301, name: 'orient', bounds: [19, 22, 78, 45] },
  { until: Infinity, name: 'royaumes', bounds: [12, 24, 52, 44] },
]

export function frameAt(year: number): Bounds {
  const frame = CAMERA_FRAMES.find((candidate) => Math.round(year) < candidate.until) ?? CAMERA_FRAMES.at(-1)
  return frame!.bounds
}

export const MIN_DISTANCE = 2.2
export const MAX_DISTANCE = 46
const FRAMING_MARGIN = 1.25

export function fitDistance(width: number, depth: number, fovDegrees: number, aspect: number): number {
  const halfTan = Math.tan((fovDegrees * Math.PI) / 360)
  const byDepth = depth / (2 * halfTan)
  const byWidth = width / (2 * halfTan * aspect)
  return Math.min(MAX_DISTANCE, Math.max(MIN_DISTANCE, Math.max(byDepth, byWidth) * FRAMING_MARGIN))
}

export function goalForBounds(bounds: Bounds, fovDegrees: number, aspect: number, depthFactor = 1): CameraGoal {
  const southWest = project(bounds[0], bounds[1])
  const northEast = project(bounds[2], bounds[3])
  const width = northEast.x - southWest.x
  const depth = (southWest.z - northEast.z) * depthFactor
  return {
    x: (southWest.x + northEast.x) / 2,
    z: (southWest.z + northEast.z) / 2,
    distance: fitDistance(width, depth, fovDegrees, aspect),
  }
}

export function goalForPlace(lon: number, lat: number, distance = 6.5): CameraGoal {
  const point = project(lon, lat)
  return { x: point.x, z: point.z, distance }
}

export function approach(current: number, target: number, deltaSeconds: number, timeConstant: number): number {
  if (timeConstant <= 0) return target
  return target + (current - target) * Math.exp(-deltaSeconds / timeConstant)
}

export function approachGoal(current: CameraGoal, target: CameraGoal, deltaSeconds: number, timeConstant: number): CameraGoal {
  return {
    x: approach(current.x, target.x, deltaSeconds, timeConstant),
    z: approach(current.z, target.z, deltaSeconds, timeConstant),
    distance: Math.exp(approach(Math.log(current.distance), Math.log(target.distance), deltaSeconds, timeConstant)),
  }
}
