import { describe, expect, it } from 'vitest'
import { eras } from '../data/eras.ts'
import { eraIndexAt, keyAction } from './keys.ts'

const width = 1000
const view = { center: -1000, span: 200 }

describe('keyAction', () => {
  it('pans toward earlier years with the left arrow', () => {
    expect(keyAction('ArrowLeft', view, width, eras)?.view.center).toBeLessThan(-1000)
    expect(keyAction('ArrowRight', view, width, eras)?.view.center).toBeGreaterThan(-1000)
  })

  it('zooms around the center', () => {
    expect(keyAction('+', view, width, eras)?.view).toEqual({ center: -1000, span: 120 })
    expect(keyAction('-', view, width, eras)?.view.span).toBeCloseTo(333.33, 1)
  })

  it('jumps between eras with page keys', () => {
    expect(eraIndexAt(-1000, eras)).toBe(1)
    const next = keyAction('PageDown', view, width, eras)?.view
    expect(next?.center).toBe((-799 + -479) / 2)
    const previous = keyAction('PageUp', view, width, eras)?.view
    expect(previous?.center).toBe((-1999 + -1099) / 2)
  })

  it('ignores other keys', () => {
    expect(keyAction('a', view, width, eras)).toBeNull()
  })
})
