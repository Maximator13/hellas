import { Battlefield, type BattleConfig } from '../battle/Battlefield.tsx'
import type { SceneProps } from '../registry.ts'
import { THERMOPYLAE } from './battle.ts'

const THERMOPYLES: BattleConfig = {
  model: 'scenes/thermopyles/thermopyles.glb',
  battle: THERMOPYLAE,
  haze: { color: '#d6dde2', density: 0.00006 },
  sunColor: '#fff2dc',
  sunIntensity: 2.6,
}

export default function Thermopyles(props: SceneProps) {
  return <Battlefield {...props} config={THERMOPYLES} />
}
