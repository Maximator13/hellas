import { readFileSync } from 'node:fs'
import { describe, expect, it } from 'vitest'
import type { HistoricalEvent } from '../src/data/schema.ts'
import { collectionSharePage, escapeHtml, sceneSharePage, sharePage, shortDescription, sitemap } from './postbuild.ts'

const template = readFileSync('index.html', 'utf8')

const gaugamela: HistoricalEvent = {
  id: 'bataille-de-gaugameles',
  title: 'Bataille de Gaugamèles',
  start: -330,
  month: 10,
  day: 1,
  precision: 'day',
  certainty: 'attested',
  era: 'classique',
  track: 'alexandre',
  category: 'war',
  importance: 2,
  summary: 'Alexandre défait l\'armée "royale" de Darius III.',
  body: 'Texte.',
  sources: [{ kind: 'ancient', author: 'Arrien', work: 'Anabase', locus: 'III, 8 à 15' }],
}

describe('share pages', () => {
  it('escapes html special characters', () => {
    expect(escapeHtml(`<a href="x">l'"&</a>`)).toBe('&#60;a href=&#34;x&#34;&#62;l&#39;&#34;&#38;&#60;/a&#62;')
  })

  it('give each event its own title, description, canonical url and social card', () => {
    const page = sharePage(template, gaugamela)
    expect(page).toContain('<title>Bataille de Gaugamèles (1er octobre 331 av. J.-C.) | Hellas</title>')
    expect(page).toContain('<meta name="description" content="Alexandre défait l&#39;armée &#34;royale&#34; de Darius III." />')
    expect(page).toContain('<link rel="canonical" href="https://maximator13.github.io/hellas/evenement/bataille-de-gaugameles/" />')
    expect(page).toContain('<meta property="og:url" content="https://maximator13.github.io/hellas/evenement/bataille-de-gaugameles/" />')
    expect(page).toContain('<meta property="og:type" content="article" />')
    expect(page).toContain('<meta name="twitter:title" content="Bataille de Gaugamèles (1er octobre 331 av. J.-C.) | Hellas" />')
  })

  it('keeps the application and adds a static cartel for crawlers', () => {
    const page = sharePage(template, gaugamela)
    expect(page).toContain('<script type="module" src="/src/main.tsx"></script>')
    expect(page).toContain('<div id="root"><article><h1>Bataille de Gaugamèles</h1>')
    expect(page).toContain('<li>Arrien, Anabase, III, 8 à 15</li>')
  })

  it('lists the home page and every event page in the sitemap', () => {
    const xml = sitemap([gaugamela], '2026-10-15')
    expect(xml).toContain('<loc>https://maximator13.github.io/hellas/</loc>')
    expect(xml).toContain('<loc>https://maximator13.github.io/hellas/evenement/bataille-de-gaugameles/</loc><lastmod>2026-10-15</lastmod>')
  })
})

describe('scene pages', () => {
  it('cuts long descriptions at a word boundary', () => {
    const text = 'mot '.repeat(60)
    const short = shortDescription(text)
    expect(short.length).toBeLessThanOrEqual(155)
    expect(short.endsWith('mot…')).toBe(true)
    expect(shortDescription('Court.')).toBe('Court.')
  })

  it('writes a share page and a sitemap entry for a scene', () => {
    const scene = { id: 'acropole', title: 'Acropole', status: 'ready' as const, year: -431, summary: 'Un sanctuaire.', points: [] }
    const page = sceneSharePage(template, scene)
    expect(page).toContain('<title>Acropole (vers 432 av. J.-C.), scène 3D | Hellas</title>')
    expect(page).toContain('https://maximator13.github.io/hellas/scene/acropole/')
    expect(sitemap([], '2026-10-19', ['scene/acropole/'])).toContain('<loc>https://maximator13.github.io/hellas/scene/acropole/</loc>')
  })

  it('writes a share page for the card collection', () => {
    const page = collectionSharePage(template)
    expect(page).toContain('<title>Collection de cartes | Hellas</title>')
    expect(page).toContain('https://maximator13.github.io/hellas/collection/')
    expect(page).toContain('href="/hellas/#/collection"')
  })
})
