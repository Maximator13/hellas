import { CanvasTexture, LinearFilter, type Texture } from 'three'
import { tracks } from '../data/tracks.ts'
import { MAP_BOUNDS } from './geo.ts'
import type { TerritorySlice } from './territories.ts'

const WIDTH = 3072
const HEIGHT = Math.round((WIDTH * (MAP_BOUNDS.north - MAP_BOUNDS.south)) / (MAP_BOUNDS.east - MAP_BOUNDS.west))
const SOFT_WIDTH = 384
const SOFT_HEIGHT = Math.round((SOFT_WIDTH * HEIGHT) / WIDTH)
const EDGE_BLUR = 2
const BORDER_WIDTH = 3.5
const SPREAD_BLUR = 22
const TRACK_ORDER = new Map(tracks.map((track, index) => [track.id, index]))
const TRACK_COLOR = new Map(tracks.map((track) => [track.id, track.color]))

interface MaskLayer {
  sharp: HTMLCanvasElement
  soft: HTMLCanvasElement
  sharpTexture: CanvasTexture
  softTexture: CanvasTexture
}

function createCanvas(width = WIDTH, height = HEIGHT): HTMLCanvasElement {
  const canvas = document.createElement('canvas')
  canvas.width = width
  canvas.height = height
  return canvas
}

function createTexture(canvas: HTMLCanvasElement): CanvasTexture {
  const texture = new CanvasTexture(canvas)
  texture.minFilter = LinearFilter
  texture.magFilter = LinearFilter
  texture.generateMipmaps = false
  return texture
}

function createLayer(): MaskLayer {
  const sharp = createCanvas()
  const soft = createCanvas(SOFT_WIDTH, SOFT_HEIGHT)
  return { sharp, soft, sharpTexture: createTexture(sharp), softTexture: createTexture(soft) }
}

function context(canvas: HTMLCanvasElement): CanvasRenderingContext2D {
  const result = canvas.getContext('2d')
  if (!result) throw new Error('Canvas 2D is not available')
  return result
}

function toPixel(lon: number, lat: number): [number, number] {
  return [
    ((lon - MAP_BOUNDS.west) / (MAP_BOUNDS.east - MAP_BOUNDS.west)) * WIDTH,
    ((MAP_BOUNDS.north - lat) / (MAP_BOUNDS.north - MAP_BOUNDS.south)) * HEIGHT,
  ]
}

function tracePolygons(ctx: CanvasRenderingContext2D, slice: TerritorySlice) {
  ctx.beginPath()
  for (const polygon of slice.polygons) {
    for (const ring of polygon) {
      ring.forEach(([lon, lat], index) => {
        const [x, y] = toPixel(lon, lat)
        if (index === 0) ctx.moveTo(x, y)
        else ctx.lineTo(x, y)
      })
      ctx.closePath()
    }
  }
}

function drawSlices(layer: MaskLayer, slices: TerritorySlice[]) {
  const scratch = createCanvas()
  const scratchContext = context(scratch)
  const ordered = slices.toSorted((a, b) => (TRACK_ORDER.get(a.track) ?? 0) - (TRACK_ORDER.get(b.track) ?? 0))
  for (const slice of ordered) {
    scratchContext.fillStyle = TRACK_COLOR.get(slice.track) ?? '#ffffff'
    tracePolygons(scratchContext, slice)
    scratchContext.fill('evenodd')
  }
  scratchContext.globalCompositeOperation = 'destination-out'
  scratchContext.lineWidth = BORDER_WIDTH
  scratchContext.lineJoin = 'round'
  for (const slice of ordered) {
    tracePolygons(scratchContext, slice)
    scratchContext.stroke()
  }
  const sharp = context(layer.sharp)
  sharp.clearRect(0, 0, WIDTH, HEIGHT)
  sharp.filter = `blur(${EDGE_BLUR}px)`
  sharp.drawImage(scratch, 0, 0)
  sharp.filter = 'none'
  const soft = context(layer.soft)
  soft.clearRect(0, 0, SOFT_WIDTH, SOFT_HEIGHT)
  soft.filter = `blur(${SPREAD_BLUR}px)`
  soft.drawImage(scratch, 0, 0, SOFT_WIDTH, SOFT_HEIGHT)
  soft.drawImage(scratch, 0, 0, SOFT_WIDTH, SOFT_HEIGHT)
  soft.filter = 'none'
  layer.sharpTexture.needsUpdate = true
  layer.softTexture.needsUpdate = true
}

function copyLayer(source: MaskLayer, target: MaskLayer) {
  for (const key of ['sharp', 'soft'] as const) {
    const ctx = context(target[key])
    ctx.clearRect(0, 0, target[key].width, target[key].height)
    ctx.drawImage(source[key], 0, 0)
  }
  target.sharpTexture.needsUpdate = true
  target.softTexture.needsUpdate = true
}

export class TerritoryMasks {
  private readonly from = createLayer()
  private readonly to = createLayer()
  private currentKey: string | null = null

  get textures(): Record<'fromSharp' | 'fromSoft' | 'toSharp' | 'toSoft', Texture> {
    return {
      fromSharp: this.from.sharpTexture,
      fromSoft: this.from.softTexture,
      toSharp: this.to.sharpTexture,
      toSoft: this.to.softTexture,
    }
  }

  show(slices: TerritorySlice[], key: string): boolean {
    if (key === this.currentKey) return false
    const first = this.currentKey === null
    this.currentKey = key
    if (!first) copyLayer(this.to, this.from)
    drawSlices(this.to, slices)
    if (first) copyLayer(this.to, this.from)
    return !first
  }

  dispose() {
    for (const layer of [this.from, this.to]) {
      layer.sharpTexture.dispose()
      layer.softTexture.dispose()
    }
  }
}
