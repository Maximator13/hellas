import { ModelScene, type ModelSceneConfig } from '../kit/ModelScene.tsx'
import type { SceneProps } from '../registry.ts'

const ARTEMISION: ModelSceneConfig = {
  model: 'scenes/artemision/artemision.glb',
  sun: { azimuth: 262, elevation: 23, color: '#ffd9a8', intensity: 2.7 },
  haze: { color: '#e4dccd', density: 0.00005 },
  overview: { azimuth: 300, elevation: 18 },
  interior: { center: [3.1, 5.1, 0], radius: 24, height: 19, ambientScale: 0.25, sunScale: 0.3 },
  lightShaftRadius: 2.4,
  sky: { turbidity: 2, rayleigh: 1 },
  exposure: 0.8,
}

export default function Artemision(props: SceneProps) {
  return <ModelScene {...props} config={ARTEMISION} />
}
