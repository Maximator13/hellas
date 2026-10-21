import { Document, Logger } from '@gltf-transform/core'
import sharp from 'sharp'
import { describe, expect, it } from 'vitest'
import { optimiseDocument } from './assets.ts'

async function textureScene(): Promise<Document> {
  const document = sceneWithMarker()
  const material = document.createMaterial('ground')
  document.getRoot().listMeshes()[0]!.listPrimitives()[0]!.setMaterial(material)
  const image = (step: number) =>
    sharp(Buffer.from(Array.from({ length: 2048 * 512 * 3 }, (_, index) => (index * step) % 251)), { raw: { width: 2048, height: 512, channels: 3 } })
      .png()
      .toBuffer()
  material.setBaseColorTexture(document.createTexture('terrain_pass').setImage(new Uint8Array(await image(37))).setMimeType('image/png'))
  material.setEmissiveTexture(document.createTexture('plaster').setImage(new Uint8Array(await image(53))).setMimeType('image/png'))
  return document
}

function sceneWithMarker(): Document {
  const document = new Document().setLogger(new Logger(Logger.Verbosity.SILENT))
  const buffer = document.createBuffer()
  const positions = document.createAccessor().setType('VEC3').setArray(new Float32Array([0, 0, 0, 1, 0, 0, 0, 1, 0])).setBuffer(buffer)
  const primitive = document.createPrimitive().setAttribute('POSITION', positions)
  const scene = document.createScene()
  scene.addChild(document.createNode('ground').setMesh(document.createMesh().addPrimitive(primitive)))
  scene.addChild(document.createNode('poi_forum').setTranslation([1, 2, 3]))
  return document
}

describe('optimiseDocument', () => {
  it('keeps the empty marker nodes that drive the camera rail', async () => {
    const document = sceneWithMarker()
    await optimiseDocument(document, false)
    const names = document.getRoot().listNodes().map((node) => node.getName())
    expect(names).toContain('poi_forum')
    expect(document.getRoot().listExtensionsUsed().map((extension) => extension.extensionName)).toContain('EXT_meshopt_compression')
  })

  it('keeps the large terrain textures above the general size cap', async () => {
    const document = await textureScene()
    await optimiseDocument(document, false)
    const widths = Object.fromEntries(
      await Promise.all(document.getRoot().listTextures().map(async (texture) => [texture.getName(), (await sharp(texture.getImage()!).metadata()).width] as const)),
    )
    expect(widths).toEqual({ terrain_pass: 2048, plaster: 1024 })
  })
})
