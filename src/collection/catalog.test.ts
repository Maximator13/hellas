import { describe, expect, it } from 'vitest'
import { cardArt } from '../data/cardArt.ts'
import { cards } from '../data/cards.ts'
import { cities, eras, people, places } from '../data/index.ts'
import { CARD_KINDS, ERA_IDS, RARITIES } from '../data/schema.ts'
import { buildCatalog, eraOf, toPool } from './catalog.ts'
import { buildSeries } from './game.ts'

const catalog = buildCatalog({ cards, art: cardArt, eras, people, cities, places })

describe('card catalog', () => {
  it('gives every card a short name and a subtitle', () => {
    for (const card of catalog) {
      expect(card.name.length, card.id).toBeLessThanOrEqual(32)
      expect(card.name, card.id).not.toMatch(/\(/)
      expect(card.subtitle.length, card.id).toBeGreaterThan(0)
    }
  })

  it('covers every rarity, kind and era', () => {
    for (const rarity of RARITIES) expect(catalog.some((card) => card.rarity === rarity), rarity).toBe(true)
    for (const kind of CARD_KINDS) expect(catalog.some((card) => card.kind === kind), kind).toBe(true)
    for (const era of ERA_IDS) expect(catalog.some((card) => card.era === era), era).toBe(true)
  })

  it('attaches an illustration only to illustrated cards', () => {
    const illustrated = new Set(cardArt.map((art) => art.card))
    for (const card of catalog) expect(card.art !== undefined, card.id).toBe(illustrated.has(card.id))
  })

  it('assigns border years to the earlier era', () => {
    expect(eraOf(-1099, eras)).toBe('bronze')
    expect(eraOf(-479, eras)).toBe('archaique')
    expect(eraOf(-322, eras)).toBe('classique')
    expect(eraOf(-29, eras)).toBe('hellenistique')
  })

  it('builds a series for every era and every kind', () => {
    const series = buildSeries(toPool(catalog), [...ERA_IDS], [...CARD_KINDS])
    expect(series.map((item) => item.id).sort()).toEqual([...ERA_IDS.map((era) => `epoque-${era}`), ...CARD_KINDS.map((kind) => `type-${kind}`)].sort())
  })
})
