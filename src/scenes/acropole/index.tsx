import { ModelScene, type ModelSceneConfig } from '../kit/ModelScene.tsx'
import type { SceneProps } from '../registry.ts'

const ACROPOLE: ModelSceneConfig = {
  model: 'scenes/acropole/acropole.glb',
  sun: { azimuth: 79, elevation: 26, color: '#fff0d6', intensity: 3.2 },
  haze: { color: '#cfdcea', density: 0.000045 },
  overview: { azimuth: 65.6, elevation: 16.2 },
  interior: { center: [7.09, 153.6, -1.64], radius: 18, height: 14, ambientScale: 0.25 },
  lightShaftRadius: 2.4,
  sky: { turbidity: 2, rayleigh: 0.9 },
  exposure: 0.85,
  views: { 'athena-de-bronze': { position: [-88, 150.5, -62], target: [-81, 150, -29] } },
}

export default function Acropole(props: SceneProps) {
  return <ModelScene {...props} config={ACROPOLE} />
}
