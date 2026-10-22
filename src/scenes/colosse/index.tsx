import { ModelScene, type ModelSceneConfig } from '../kit/ModelScene.tsx'
import type { SceneProps } from '../registry.ts'

const COLOSSE: ModelSceneConfig = {
  model: 'scenes/colosse/colosse.glb',
  sun: { azimuth: 75, elevation: 19, color: '#ffe2b8', intensity: 3.2 },
  haze: { color: '#d3deea', density: 0.00004 },
  overview: { azimuth: 40, elevation: 14 },
  sky: { turbidity: 2, rayleigh: 0.9 },
  exposure: 0.85,
}

export default function Colosse(props: SceneProps) {
  return <ModelScene {...props} config={COLOSSE} />
}
