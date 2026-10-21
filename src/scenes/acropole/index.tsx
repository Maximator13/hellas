import { ModelScene, type ModelSceneConfig } from '../kit/ModelScene.tsx'
import type { SceneProps } from '../registry.ts'

const ACROPOLE: ModelSceneConfig = {
  model: 'scenes/acropole/acropole.glb',
  sun: { azimuth: 79, elevation: 26, color: '#fff0d6', intensity: 3.2 },
  haze: { color: '#cfdcea', density: 0.000045 },
  overview: { azimuth: 225, elevation: 32 },
  interior: { center: [0, 14, 0], radius: 16, height: 14, ambientScale: 0.25 },
  lightShaftRadius: 2.4,
}

export default function Acropole(props: SceneProps) {
  return <ModelScene {...props} config={ACROPOLE} />
}
