import { useEffect, useMemo } from 'react'
import { BackSide, ShaderMaterial, type Vector3 } from 'three'

const vertexShader = `
varying vec3 vDirection;
void main() {
  vDirection = normalize(position);
  vec4 world = modelMatrix * vec4(position, 1.0);
  gl_Position = projectionMatrix * viewMatrix * world;
  gl_Position.z = gl_Position.w;
}
`

const fragmentShader = `
uniform vec3 sunDirection;
uniform vec3 moonDirection;
uniform float glowStrength;
varying vec3 vDirection;
void main() {
  vec3 d = normalize(vDirection);
  float h = d.y;
  float up = max(h, 0.0);
  vec3 zenith = vec3(0.006, 0.022, 0.065);
  vec3 horizon = vec3(0.045, 0.085, 0.150);
  vec3 colour = mix(horizon, zenith, smoothstep(0.0, 0.55, up));
  vec2 planar = normalize(d.xz + vec2(1e-5));
  vec2 sunFlat = normalize(sunDirection.xz + vec2(1e-5));
  float toward = max(dot(planar, sunFlat), 0.0);
  float band = exp(-up * 9.0);
  vec3 ember = mix(vec3(0.10, 0.06, 0.10), vec3(0.95, 0.42, 0.14), exp(-up * 30.0));
  colour += ember * pow(toward, 3.0) * band * glowStrength;
  colour += vec3(0.05, 0.035, 0.04) * pow(toward, 1.2) * exp(-up * 4.0) * glowStrength;
  float moon = dot(d, moonDirection);
  vec3 moonTint = mix(vec3(1.0, 0.78, 0.55), vec3(1.0, 0.96, 0.9), smoothstep(0.05, 0.4, moonDirection.y));
  colour += moonTint * smoothstep(0.99994, 0.99997, moon) * 6.0;
  colour += vec3(0.08, 0.09, 0.12) * pow(max(moon, 0.0), 300.0);
  if (h < 0.0) colour = mix(colour, horizon * 0.5, smoothstep(0.0, -0.08, h));
  gl_FragColor = vec4(colour, 1.0);
}
`

export function TwilightSky({ radius, sun, moon }: { radius: number; sun: Vector3; moon: Vector3 }) {
  const material = useMemo(
    () =>
      new ShaderMaterial({
        vertexShader,
        fragmentShader,
        side: BackSide,
        depthWrite: false,
        fog: false,
        uniforms: {
          sunDirection: { value: sun.clone().normalize() },
          moonDirection: { value: moon.clone().normalize() },
          glowStrength: { value: Math.min(1, Math.max(0, 1 + (Math.asin(sun.y / sun.length()) * 180) / Math.PI / 18)) },
        },
      }),
    [sun, moon],
  )
  useEffect(() => () => material.dispose(), [material])
  return (
    <mesh scale={radius} frustumCulled={false} renderOrder={-1} material={material}>
      <sphereGeometry args={[1, 48, 24]} />
    </mesh>
  )
}
