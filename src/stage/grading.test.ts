import { describe, expect, it } from 'vitest'
import { FIRST_YEAR, LAST_YEAR } from '../core/dates.ts'
import { eras } from '../data/eras.ts'
import { BACKGROUND, ERA_GRADING, contrastRatio, gradingAt, mixGrading, readableAccent, rgbToCss } from './grading.ts'

describe('gradingAt', () => {
  it('uses the era grading well inside an era', () => {
    expect(gradingAt(-1500, eras)).toEqual(ERA_GRADING.bronze)
    expect(gradingAt(-400, eras)).toEqual(ERA_GRADING.classique)
    expect(gradingAt(-100, eras)).toEqual(ERA_GRADING.hellenistique)
  })

  it('blends two eras halfway at their boundary', () => {
    const boundary = gradingAt(-479, eras)
    const halfway = mixGrading(ERA_GRADING.archaique, ERA_GRADING.classique, 0.5)
    expect(boundary.exposure).toBeCloseTo(halfway.exposure)
    expect(boundary.accent[0]).toBeCloseTo(halfway.accent[0])
  })

  it('moves monotonically across a boundary', () => {
    const values = [-515, -495, -479, -465, -445].map((year) => gradingAt(year, eras).saturation)
    const falling = values.every((value, index) => index === 0 || value <= values[index - 1]!)
    expect(falling).toBe(true)
  })
})

describe('rgbToCss', () => {
  it('clamps channels', () => {
    expect(rgbToCss([1.2, 0.5, -0.1])).toBe('rgb(255 128 0)')
  })
})

describe('readableAccent', () => {
  it('keeps text and markers readable on the dark background in every era and transition', () => {
    for (let year = FIRST_YEAR; year <= LAST_YEAR; year += 7) {
      const accent = readableAccent(gradingAt(year, eras).accent)
      expect(contrastRatio(accent, BACKGROUND)).toBeGreaterThanOrEqual(4.5)
    }
  })

  it('computes the reference contrast of black on white', () => {
    expect(contrastRatio([1, 1, 1], [0, 0, 0])).toBeCloseTo(21)
  })
})
