import type { Era, EraId } from '../data/schema.ts'

export type Rgb = [number, number, number]

export interface Grading {
  exposure: number
  contrast: number
  saturation: number
  lift: Rgb
  gain: Rgb
  skyTop: Rgb
  skyHorizon: Rgb
  fog: Rgb
  sun: Rgb
  sunElevation: number
  accent: Rgb
}

export const ERA_GRADING: Record<EraId, Grading> = {
  bronze: {
    exposure: 1.0,
    contrast: 1.08,
    saturation: 1.25,
    lift: [0.04, 0.02, 0.0],
    gain: [1.12, 0.98, 0.84],
    skyTop: [0.22, 0.36, 0.62],
    skyHorizon: [0.98, 0.7, 0.42],
    fog: [0.86, 0.62, 0.42],
    sun: [1.0, 0.78, 0.5],
    sunElevation: 0.18,
    accent: [0.86, 0.42, 0.22],
  },
  'ages-obscurs': {
    exposure: 0.88,
    contrast: 1.1,
    saturation: 0.98,
    lift: [0.04, 0.02, 0.01],
    gain: [1.08, 0.95, 0.82],
    skyTop: [0.16, 0.18, 0.26],
    skyHorizon: [0.7, 0.5, 0.34],
    fog: [0.46, 0.36, 0.28],
    sun: [1.0, 0.66, 0.38],
    sunElevation: 0.08,
    accent: [0.8, 0.54, 0.3],
  },
  archaique: {
    exposure: 1.04,
    contrast: 1.08,
    saturation: 1.3,
    lift: [0.01, 0.02, 0.04],
    gain: [1.04, 1.0, 0.96],
    skyTop: [0.2, 0.46, 0.86],
    skyHorizon: [0.88, 0.86, 0.8],
    fog: [0.78, 0.8, 0.82],
    sun: [1.0, 0.93, 0.82],
    sunElevation: 0.4,
    accent: [0.88, 0.34, 0.28],
  },
  classique: {
    exposure: 1.08,
    contrast: 1.1,
    saturation: 1.22,
    lift: [0.0, 0.01, 0.03],
    gain: [1.0, 1.0, 1.02],
    skyTop: [0.12, 0.42, 0.9],
    skyHorizon: [0.84, 0.9, 0.96],
    fog: [0.8, 0.86, 0.92],
    sun: [1.0, 0.98, 0.94],
    sunElevation: 0.8,
    accent: [0.36, 0.66, 0.95],
  },
  hellenistique: {
    exposure: 1.02,
    contrast: 1.1,
    saturation: 1.25,
    lift: [0.03, 0.01, 0.04],
    gain: [1.12, 0.98, 0.86],
    skyTop: [0.24, 0.36, 0.7],
    skyHorizon: [1.0, 0.78, 0.5],
    fog: [0.9, 0.74, 0.56],
    sun: [1.0, 0.82, 0.52],
    sunElevation: 0.25,
    accent: [0.92, 0.74, 0.3],
  },
}

export const SCENE_LOOK = { exposure: 1 }

const TRANSITION_YEARS = 20

function mix(a: number, b: number, t: number): number {
  return a * (1 - t) + b * t
}

function mixRgb(a: Rgb, b: Rgb, t: number): Rgb {
  return [mix(a[0], b[0], t), mix(a[1], b[1], t), mix(a[2], b[2], t)]
}

export function mixGrading(a: Grading, b: Grading, t: number): Grading {
  return {
    exposure: mix(a.exposure, b.exposure, t),
    contrast: mix(a.contrast, b.contrast, t),
    saturation: mix(a.saturation, b.saturation, t),
    lift: mixRgb(a.lift, b.lift, t),
    gain: mixRgb(a.gain, b.gain, t),
    skyTop: mixRgb(a.skyTop, b.skyTop, t),
    skyHorizon: mixRgb(a.skyHorizon, b.skyHorizon, t),
    fog: mixRgb(a.fog, b.fog, t),
    sun: mixRgb(a.sun, b.sun, t),
    sunElevation: mix(a.sunElevation, b.sunElevation, t),
    accent: mixRgb(a.accent, b.accent, t),
  }
}

function smoothstep(edge0: number, edge1: number, value: number): number {
  const t = Math.min(1, Math.max(0, (value - edge0) / (edge1 - edge0)))
  return t * t * (3 - 2 * t)
}

export function gradingAt(year: number, eras: Era[]): Grading {
  const ordered = [...eras].sort((a, b) => a.start - b.start)
  let grading = ERA_GRADING[ordered[0]!.id]
  for (const era of ordered.slice(1)) {
    const window = Math.min(TRANSITION_YEARS, (era.end - era.start) / 4)
    const t = smoothstep(era.start - window, era.start + window, year)
    grading = mixGrading(grading, ERA_GRADING[era.id], t)
  }
  return grading
}

export function rgbToCss([r, g, b]: Rgb): string {
  const channel = (value: number) => Math.round(Math.min(1, Math.max(0, value)) * 255)
  return `rgb(${channel(r)} ${channel(g)} ${channel(b)})`
}

export const BACKGROUND: Rgb = [0.07, 0.05, 0.04]

function relativeLuminance([r, g, b]: Rgb): number {
  const linear = (value: number) => (value <= 0.04045 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4)
  return 0.2126 * linear(r) + 0.7152 * linear(g) + 0.0722 * linear(b)
}

export function contrastRatio(a: Rgb, b: Rgb): number {
  const [light, dark] = [relativeLuminance(a), relativeLuminance(b)].sort((x, y) => y - x)
  return (light! + 0.05) / (dark! + 0.05)
}

export function readableAccent(accent: Rgb): Rgb {
  return mixRgb(accent, [1, 1, 1], 0.4)
}
