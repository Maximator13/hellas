import { ModelScene, type ModelSceneConfig } from '../kit/ModelScene.tsx'
import type { SceneProps } from '../registry.ts'

const PHARE: ModelSceneConfig = {
  model: 'scenes/phare/phare.glb',
  sun: { azimuth: 105, elevation: 9, color: '#a9c2e4', intensity: 2.4 },
  skySun: { azimuth: 288, elevation: -6 },
  haze: { color: '#1c2a3a', density: 0.00008 },
  overview: { azimuth: 110, elevation: 8 },
  exposure: 1.0,
}

export default function Phare(props: SceneProps) {
  return <ModelScene {...props} config={PHARE} />
}
