import { readFileSync } from 'node:fs'
import { describe, expect, it } from 'vitest'
import { scenes } from '../../data/scenes.ts'
import { THERMOPYLAE } from '../thermopyles/battle.ts'
import { rasterize, heightAt } from './heightfield.ts'
import { parseBattle, type Unit } from './schema.ts'
import {
  deathTimes,
  figureCount,
  isShown,
  lerpAngle,
  placeFigure,
  pointForTime,
  slotsFor,
  stateAt,
  sunAt,
  timeForPoint,
  trackOf,
  type UnitState,
} from './timeline.ts'

const unit: Unit = {
  id: 'essai',
  label: 'Essai',
  side: 'a',
  troop: 'hastatus',
  soldiers: 200,
  start: { at: [0, 0], facing: 180, width: 100, depth: 20 },
  moves: [
    { phase: 1, at: [0, -100], action: 'march' },
    { phase: 2 },
    { phase: 3, via: [[100, -100]], at: [100, 0], facing: 90, losses: 0.5, action: 'fight' },
  ],
}

describe('battle timeline', () => {
  it('interpolates between keyframes and holds in between', () => {
    const track = trackOf(unit)
    const state = {} as UnitState
    expect(stateAt(track, 0, state).y).toBe(0)
    expect(stateAt(track, 0.5, state).y).toBeCloseTo(-50)
    expect(stateAt(track, 0.5, state).action).toBe('march')
    expect(stateAt(track, 1.5, state).y).toBeCloseTo(-100)
    expect(stateAt(track, 1.5, state).action).toBe('stand')
    expect(stateAt(track, 3, state)).toMatchObject({ x: 100, y: 0, facing: 90, losses: 0.5, action: 'fight' })
    expect(stateAt(track, 2.5, state).x).toBeCloseTo(100, 0)
  })

  it('keeps every figure inside its formation', () => {
    const slots = slotsFor(10, 100, 20, 1)
    const state = stateAt(trackOf(unit), 0, {} as UnitState)
    for (const slot of slots) {
      const placed = placeFigure(state, slot, { x: 0, y: 0, heading: 0 })
      expect(Math.abs(placed.x)).toBeLessThan(52)
      expect(Math.abs(placed.y)).toBeLessThan(12)
    }
  })

  it('kills the expected share of figures by the end', () => {
    const times = deathTimes(trackOf(unit), 100, 3, 1)
    const dead = [...times].filter((time) => time <= 3).length
    expect(dead).toBe(50)
    expect(Math.min(...times)).toBeGreaterThan(2)
  })

  it('maps time and scene points both ways', () => {
    expect(pointForTime(0, 8)).toBe(0)
    expect(pointForTime(0.01, 8)).toBe(1)
    expect(pointForTime(3, 8)).toBe(4)
    expect(pointForTime(8, 8)).toBe(8)
    expect(pointForTime(timeForPoint(5, false), 8)).toBe(5)
    expect(pointForTime(timeForPoint(5, true) - 1e-4, 8)).toBe(5)
  })

  it('turns by the shortest way', () => {
    expect(lerpAngle(350, 10, 0.5)).toBeCloseTo(360)
    expect((lerpAngle(90, 270, 1) + 360) % 360).toBeCloseTo(270)
  })

  it('places the summer sun of Cannae', () => {
    const noon = sunAt(12, 41.3, 21)
    expect(noon.azimuth).toBeCloseTo(180)
    expect(noon.elevation).toBeCloseTo(69.7, 0)
    expect(sunAt(8, 41.3, 21).azimuth).toBeGreaterThan(85)
    expect(sunAt(8, 41.3, 21).azimuth).toBeLessThan(100)
  })
})

describe('battle columns and camps', () => {
  const column: Unit = {
    id: 'colonne',
    label: 'Colonne',
    side: 'b',
    troop: 'immortel',
    soldiers: 100,
    start: { at: [0, 0], facing: 90, width: 20, depth: 20, action: 'camp' },
    moves: [
      { phase: 1 },
      { phase: 2, via: [[1000, 0]], at: [1000, 1000], width: 4, depth: 600, action: 'march', column: true },
      { phase: 3, at: [1000, 1500] },
      { phase: 4, at: [1000, 1500], width: 50, depth: 20, action: 'surrender', column: false },
    ],
  }

  it('strings a column along its route behind the head', () => {
    const track = trackOf(column)
    const state = stateAt(track, 2, {} as UnitState)
    expect(state).toMatchObject({ x: 1000, y: 1000, column: 1 })
    const head = placeFigure(state, { u: 0.5, v: 0, rank: 0, jitterX: 0, jitterY: 0, phase: 0 }, { x: 0, y: 0, heading: 0 })
    const tail = placeFigure(state, { u: 0.5, v: 1, rank: 1, jitterX: 0, jitterY: 0, phase: 0 }, { x: 0, y: 0, heading: 0 })
    expect(head.x).toBeCloseTo(1000)
    expect(head.y).toBeCloseTo(1000)
    expect(tail.x).toBeCloseTo(1000)
    expect(tail.y).toBeCloseTo(400)
    expect(tail.heading).toBeCloseTo(0)
  })

  it('extends the route when a column keeps marching', () => {
    const state = stateAt(trackOf(column), 3, {} as UnitState)
    const tail = placeFigure(state, { u: 0.5, v: 1, rank: 1, jitterX: 0, jitterY: 0, phase: 0 }, { x: 0, y: 0, heading: 0 })
    expect(state.head).toBeCloseTo(2500)
    expect(tail.x).toBeCloseTo(1000)
    expect(tail.y).toBeCloseTo(900)
  })

  it('hides camped units and holds a surrender', () => {
    const track = trackOf(column)
    expect(isShown(stateAt(track, 0.5, {} as UnitState))).toBe(false)
    expect(isShown(stateAt(track, 1.5, {} as UnitState))).toBe(true)
    expect(stateAt(track, 4, {} as UnitState)).toMatchObject({ action: 'surrender', column: 0 })
    expect(parseBattle({ ...THERMOPYLAE, units: [...THERMOPYLAE.units, column] }).units.at(-1)!.moves[1]!.column).toBe(true)
  })
})

describe('height field', () => {
  it('rasterizes a sloping square', () => {
    const positions = [0, 0, 0, 10, 10, 0, 10, 10, 10, 0, 0, 10]
    const field = rasterize(positions, [0, 3, 1, 1, 3, 2], 1)
    expect(heightAt(field, 5, 5)).toBeCloseTo(5)
    expect(heightAt(field, 2.5, 7)).toBeCloseTo(2.5)
  })
})

describe('Thermopylae data', () => {
  const kinds = [...readFileSync(new URL('../../../blender/kit/figures.py', import.meta.url), 'utf8').matchAll(/^ {4}"([a-z-]+)": \(/gm)].map((match) => match[1])

  it('is a valid battle', () => {
    expect(() => parseBattle(THERMOPYLAE)).not.toThrow()
  })

  it('has one scene point per phase, in the same order', () => {
    const scene = scenes.find((item) => item.id === 'thermopyles')
    expect(scene?.points?.map((point) => point.id)).toEqual(THERMOPYLAE.phases.map((phase) => phase.id))
  })

  it('uses only figurines made in Blender', () => {
    expect(kinds).toContain('hoplite-spartiate')
    for (const item of THERMOPYLAE.units) expect(kinds).toContain(item.troop)
  })

  it('fields 7 100 Greeks and 56 000 Persians', () => {
    const total = (side: Unit['side']) => THERMOPYLAE.units.filter((item) => item.side === side).reduce((sum, item) => sum + item.soldiers, 0)
    expect(total('a')).toBe(7100)
    expect(total('b')).toBe(56000)
  })

  it('keeps every ground view on a unit that is on the field', () => {
    THERMOPYLAE.phases.forEach((phase, index) => {
      const unit = THERMOPYLAE.units.find((item) => item.id === phase.ground.unit)!
      expect(isShown(stateAt(trackOf(unit), index + 0.5, {} as UnitState))).toBe(true)
    })
  })

  it('draws at most about 7 600 figurines at once at one figurine for 5 soldiers', () => {
    const phases = THERMOPYLAE.phases.length
    const units = THERMOPYLAE.units.map((item, index) => {
      const track = trackOf(item)
      const count = figureCount(item, THERMOPYLAE.scale)
      return { track, deaths: [...deathTimes(track, count, phases, index + 1)] }
    })
    let peak = 0
    for (let time = 0; time <= phases; time += 0.05) {
      const shown = units.reduce((sum, { track, deaths }) => {
        const living = isShown(stateAt(track, time, {} as UnitState))
        return sum + deaths.filter((death) => death <= time || living).length
      }, 0)
      peak = Math.max(peak, shown)
    }
    expect(units.reduce((sum, { deaths }) => sum + deaths.length, 0)).toBe(12620)
    expect(peak).toBeLessThanOrEqual(7600)
  })
})
