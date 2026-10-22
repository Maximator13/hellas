import { ModelScene, type ModelSceneConfig } from '../kit/ModelScene.tsx'
import type { SceneProps } from '../registry.ts'

const MAUSOLEE: ModelSceneConfig = {
  model: 'scenes/mausolee/mausolee.glb',
  sun: { azimuth: 121, elevation: 34, color: '#fff2dc', intensity: 3.1 },
  haze: { color: '#d4dfea', density: 0.00004 },
  overview: { azimuth: 170, elevation: 12 },
  interior: { center: [0, 32.6, 0], radius: 18, height: 12, ambientScale: 0.55, sunScale: 0.6 },
  sky: { turbidity: 2.2, rayleigh: 0.9 },
  exposure: 0.85,
}

export default function Mausolee(props: SceneProps) {
  return <ModelScene {...props} config={MAUSOLEE} />
}
