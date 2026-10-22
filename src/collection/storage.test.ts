import { describe, expect, it } from 'vitest'
import { parseExplore, withVisit } from '../core/explore.ts'
import { emptyState } from './game.ts'
import { loadState, newPlayerId, parseState, saveState, STORAGE_KEY, type KeyValueStore } from './storage.ts'

function memoryStore(): KeyValueStore & { data: Map<string, string> } {
  const data = new Map<string, string>()
  return {
    data,
    getItem: (key) => data.get(key) ?? null,
    setItem: (key, value) => {
      data.set(key, value)
    },
  }
}

describe('collection storage', () => {
  it('saves and reloads the same state', () => {
    const store = memoryStore()
    const state = { ...emptyState('abc'), owned: { pericles: '2026-10-22' }, drachmes: 42, lastDaily: '2026-10-22', bonusPacks: 1 }
    expect(saveState(store, state)).toBe(true)
    expect(loadState(store)).toEqual(state)
    expect(JSON.parse(store.data.get(STORAGE_KEY) ?? '{}').version).toBe(1)
  })

  it('starts a fresh collection from missing or corrupt data', () => {
    expect(parseState(null, 'neuf')).toEqual(emptyState('neuf'))
    expect(parseState('{pas du json', 'neuf')).toEqual(emptyState('neuf'))
    expect(parseState(JSON.stringify({ version: 2, player: 'x' }), 'neuf')).toEqual(emptyState('neuf'))
  })

  it('drops invalid fields', () => {
    const raw = JSON.stringify({ version: 1, player: 'p', owned: { a: '2026-10-22', b: 3 }, drachmes: -5, sinceEpic: 2.5, rewardedEvents: ['x', 4] })
    const state = parseState(raw, 'neuf')
    expect(state.owned).toEqual({ a: '2026-10-22' })
    expect(state.drachmes).toBe(0)
    expect(state.sinceEpic).toBe(0)
    expect(state.rewardedEvents).toEqual(['x'])
  })

  it('survives a storage that refuses to read or write', () => {
    const broken: KeyValueStore = {
      getItem: () => {
        throw new Error('blocked')
      },
      setItem: () => {
        throw new Error('quota')
      },
    }
    expect(saveState(broken, emptyState('p'))).toBe(false)
    expect(loadState(broken).owned).toEqual({})
    expect(saveState(null, emptyState('p'))).toBe(false)
  })

  it('creates readable player ids', () => {
    expect(newPlayerId()).toMatch(/^[a-z0-9]{12}$/)
  })
})

describe('exploration log', () => {
  it('records scenes and events once and ignores other routes', () => {
    let log = parseExplore(null)
    log = withVisit(log, { name: 'scene', id: 'acropole' })
    log = withVisit(log, { name: 'scene', id: 'acropole' })
    log = withVisit(log, { name: 'event', id: 'bataille-de-salamine' })
    expect(withVisit(log, { name: 'home' })).toBe(log)
    expect(log).toEqual({ scenes: ['acropole'], events: ['bataille-de-salamine'] })
    expect(parseExplore('[1,2]')).toEqual({ scenes: [], events: [] })
    expect(parseExplore('nope')).toEqual({ scenes: [], events: [] })
  })
})
