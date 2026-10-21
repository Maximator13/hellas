import { describe, expect, it } from 'vitest'
import { dataset } from './index.ts'
import { validateDataset } from './validate.ts'

describe('project data', () => {
  it('passes schema, reference and style validation', () => {
    expect(validateDataset(dataset)).toEqual([])
  })
})

describe('validateDataset', () => {
  const valid = structuredClone(dataset)

  it('reports an event outside its era and an inactive track', () => {
    const broken = {
      ...valid,
      events: [
        {
          id: 'evenement-faux',
          title: 'Faux',
          start: -100,
          precision: 'year',
          certainty: 'attested',
          era: 'bronze',
          track: 'minoens',
          category: 'politics',
          importance: 3,
          summary: 'Résumé.',
          body: 'Texte.',
          sources: [{ kind: 'modern', author: 'Auteur', work: 'Ouvrage' }],
        },
      ],
    }
    expect(validateDataset(broken)).toEqual([
      'event evenement-faux: start outside era bronze',
      'event evenement-faux: track minoens inactive at start',
    ])
  })

  it('reports forbidden dashes anywhere in the data', () => {
    const dash = String.fromCharCode(0x2014)
    const broken = { ...valid, eras: valid.eras.map((era, index) => (index === 0 ? { ...era, name: `Bronze ${dash} récent` } : era)) }
    expect(validateDataset(broken)).toEqual(['data.eras[0].name: em or en dash'])
  })

  it('reports schema problems with the item id', () => {
    const broken = { ...valid, scenes: [{ id: 'Acropole', title: 'Acropole', status: 'planned' }] }
    expect(validateDataset(broken)[0]).toMatch(/^scene Acropole: id /)
  })
})

describe('scene rules', () => {
  const valid = structuredClone(dataset)

  it('requires date, place, summary and points for a ready scene', () => {
    const broken = { ...valid, scenes: [...valid.scenes, { id: 'essai', title: 'Essai', status: 'ready' }] }
    expect(validateDataset(broken)).toEqual([
      'scene essai: ready scene without year',
      'scene essai: ready scene without lat',
      'scene essai: ready scene without lon',
      'scene essai: ready scene without summary',
      'scene essai: ready scene without points',
    ])
  })

  it('reports duplicate points of interest', () => {
    const point = { id: 'forum', title: 'Forum', text: 'Texte.', sources: ['Source'] }
    const broken = { ...valid, scenes: [...valid.scenes, { id: 'essai', title: 'Essai', status: 'planned', points: [point, point] }] }
    expect(validateDataset(broken)).toEqual(['scene essai: duplicate point forum'])
  })
})

describe('phase 1 coverage', () => {
  it('has about twenty events with at least three in every era', () => {
    expect(dataset.events.length).toBeGreaterThanOrEqual(20)
    for (const era of dataset.eras) {
      expect(dataset.events.filter((event) => event.era === era.id).length).toBeGreaterThanOrEqual(3)
    }
  })
})
