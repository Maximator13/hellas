import { describe, expect, it } from 'vitest'
import { cardArtErrors, sceneFileErrors } from './validate-data.ts'

describe('sceneFileErrors', () => {
  const files = new Set(['src/scenes/nimes/index.tsx', 'blender/nimes.py', 'src/scenes/arles/index.tsx', 'src/scenes/pont-du-gard/index.tsx', 'blender/pont_du_gard.py'])
  const exists = (path: string) => files.has(path)

  it('accepts planned scenes without files and complete ready scenes', () => {
    const scenes = [
      { id: 'nimes', status: 'ready' },
      { id: 'cannes', status: 'planned' },
      { id: 'arles', status: 'planned' },
      { id: 'pont-du-gard', status: 'ready' },
    ]
    expect(sceneFileErrors(scenes, ['kit', 'battle', 'nimes', 'arles', 'pont-du-gard'], exists)).toEqual([])
  })

  it('reports a ready scene without its Blender script and a folder without data', () => {
    const scenes = [{ id: 'arles', status: 'ready' }]
    expect(sceneFileErrors(scenes, ['kit', 'arles', 'ostie'], exists)).toEqual([
      'scene arles: ready scene without blender/arles.py',
      'src/scenes/ostie: no matching entry in src/data/scenes.ts',
    ])
  })
})

describe('cardArtErrors', () => {
  it('reports the missing image files of an illustrated card only', () => {
    const exists = (path: string) => path === 'public/cards/pericles.webp'
    expect(cardArtErrors(['pericles'], exists)).toEqual(['card pericles: missing public/cards/pericles-s.webp'])
    expect(cardArtErrors([], exists)).toEqual([])
  })
})
