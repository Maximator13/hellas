import { Billboard, Text } from '@react-three/drei'
import { useFrame } from '@react-three/fiber'
import { useMemo, useRef } from 'react'
import { Vector3, type Group } from 'three'
import displayFontUrl from '@fontsource/didact-gothic/files/didact-gothic-latin-400-normal.woff?url'
import { prefersReducedMotion } from '../core/motion.ts'
import type { Track } from '../data/schema.ts'
import { tracks } from '../data/tracks.ts'
import { useApp } from '../store.ts'
import { project } from './geo.ts'
import type { HeightSampler } from './reliefSampler.ts'
import type { TerritorySlice } from './territories.ts'

const LABEL_SCALE = 0.02
const LIFT = 0.25
const FADE_SECONDS = 0.8

function TrackLabel({ track, slices, height }: { track: Track; slices: TerritorySlice[]; height: HeightSampler }) {
  const group = useRef<Group>(null)
  const label = useRef<{ fillOpacity: number; outlineOpacity: number } | null>(null)
  const opacity = useRef(0)
  const target = useMemo(() => new Vector3(), [])
  const reducedMotion = useMemo(() => prefersReducedMotion(), [])

  useFrame(({ camera }, delta) => {
    const current = group.current
    if (!current) return
    const year = Math.round(useApp.getState().view.center)
    const slice = slices.find((candidate) => year >= candidate.from && year <= candidate.to)
    if (slice) {
      const [lon, lat] = slice.label
      const point = project(lon, lat)
      target.set(point.x, height(lon, lat) + LIFT, point.z)
      if (opacity.current < 0.01) current.position.copy(target)
      else current.position.lerp(target, reducedMotion ? 1 : Math.min(1, delta * 3))
    }
    const step = reducedMotion ? 1 : delta / FADE_SECONDS
    opacity.current = slice ? Math.min(1, opacity.current + step) : Math.max(0, opacity.current - step)
    current.visible = opacity.current > 0.01
    current.scale.setScalar(camera.position.distanceTo(current.position) * LABEL_SCALE)
    if (label.current) {
      label.current.fillOpacity = opacity.current * 0.95
      label.current.outlineOpacity = opacity.current * 0.7
    }
  })

  return (
    <group ref={group} visible={false}>
      <Billboard>
        <Text
          ref={label}
          font={displayFontUrl}
          fontSize={0.62}
          letterSpacing={0.18}
          color={track.color}
          outlineWidth={0.05}
          outlineColor="#0b1117"
          anchorX="center"
          anchorY="middle"
          fillOpacity={0}
          outlineOpacity={0}
        >
          {track.name.replace(/\s*\(.*\)$/, '').toUpperCase()}
        </Text>
      </Billboard>
    </group>
  )
}

export function TerritoryLabels({ slices, height }: { slices: TerritorySlice[]; height: HeightSampler }) {
  const byTrack = useMemo(
    () => tracks.map((track) => ({ track, slices: slices.filter((slice) => slice.track === track.id) })).filter((entry) => entry.slices.length > 0),
    [slices],
  )
  return (
    <>
      {byTrack.map(({ track, slices: own }) => (
        <TrackLabel key={track.id} track={track} slices={own} height={height} />
      ))}
    </>
  )
}
