import { ModelScene, type ModelSceneConfig } from '../kit/ModelScene.tsx'
import type { SceneProps } from '../registry.ts'

const OLYMPIE: ModelSceneConfig = {
  model: 'scenes/olympie/olympie.glb',
  sun: { azimuth: 90, elevation: 27, color: '#fff0d4', intensity: 3.2 },
  haze: { color: '#d6dde6', density: 0.00005 },
  overview: { azimuth: 128, elevation: 20 },
  interior: { center: [0, 36.4, 0], radius: 15, height: 15, ambientScale: 0.3, sunScale: 0.3 },
  lightShaftRadius: 2.2,
  sky: { turbidity: 2.4, rayleigh: 0.9 },
  exposure: 0.85,
}

export default function Olympie(props: SceneProps) {
  return <ModelScene {...props} config={OLYMPIE} />
}
