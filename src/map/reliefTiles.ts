import { DataTexture, LinearFilter, LinearMipmapLinearFilter, RedFormat, UnsignedByteType } from 'three'
import { RELIEF_GRID, RELIEF_TILE_COLUMNS, type ReliefTile } from './geo.ts'

const pending = new Map<ReliefTile, Promise<Uint8Array>>()

async function decodeTile(tile: ReliefTile): Promise<Uint8Array> {
  const response = await fetch(`${import.meta.env.BASE_URL}geo/relief-${tile}.webp`)
  if (!response.ok) throw new Error(`relief ${tile} answered ${response.status}`)
  const bitmap = await createImageBitmap(await response.blob(), { colorSpaceConversion: 'none', premultiplyAlpha: 'none' })
  const canvas = document.createElement('canvas')
  canvas.width = bitmap.width
  canvas.height = bitmap.height
  const context = canvas.getContext('2d', { willReadFrequently: true })
  if (!context) throw new Error('Canvas 2D is not available')
  context.drawImage(bitmap, 0, 0)
  bitmap.close()
  const rgba = context.getImageData(0, 0, canvas.width, canvas.height).data
  const pixels = new Uint8Array(canvas.width * canvas.height)
  for (let index = 0; index < pixels.length; index++) pixels[index] = rgba[index * 4] ?? 0
  return pixels
}

export function loadReliefTile(tile: ReliefTile): Promise<Uint8Array> {
  let promise = pending.get(tile)
  if (!promise) {
    promise = decodeTile(tile)
    pending.set(tile, promise)
  }
  return promise
}

export function reliefTexture(pixels: Uint8Array | null): DataTexture {
  const texture = pixels
    ? new DataTexture(pixels, RELIEF_TILE_COLUMNS, RELIEF_GRID.rows, RedFormat, UnsignedByteType)
    : new DataTexture(new Uint8Array([127]), 1, 1, RedFormat, UnsignedByteType)
  texture.minFilter = pixels ? LinearMipmapLinearFilter : LinearFilter
  texture.magFilter = LinearFilter
  texture.generateMipmaps = pixels !== null
  texture.needsUpdate = true
  return texture
}
