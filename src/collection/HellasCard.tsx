import type { PointerEvent } from 'react'
import { frenchSpacing } from '../core/typography.ts'
import { ERA_SHORT, KIND_LABEL, RARITY_LABEL } from '../data/collectionUi.ts'
import type { CardKind } from '../data/schema.ts'
import { SITE } from '../site.ts'
import type { CardView } from './catalog.ts'
import { rank } from './game.ts'

const KIND_ICON: Record<CardKind, string> = {
  person: 'M12 3a4 4 0 1 1 0 8a4 4 0 0 1 0-8zm-7 18c0-4 3.1-7 7-7s7 3 7 7z',
  place: 'M3 21h18v-2H3zm2-3h2v-7H5zm4 0h2v-7H9zm4 0h2v-7h-2zm4 0h2v-7h-2zM2 10h20L12 3z',
  relic: 'M9 2h6v2l-1 1v2c3 1 5 4 5 8c0 4-3 7-7 7s-7-3-7-7c0-4 2-7 5-8V5L9 4z',
  unit: 'M12 2l8 3v6c0 5-3.4 9.4-8 11c-4.6-1.6-8-6-8-11V5zm0 4l-3 3l3 3l3-3z',
  deity: 'M12 1l1.8 4.6L18.5 4l-1.6 4.7L22 10l-4.7 1.6L19 16.5l-4.6-1.8L12 19l-2.4-4.3L5 16.5l1.7-4.9L2 10l5.1-1.3L5.5 4l4.7 1.6zM12 8a3 3 0 1 0 0 6a3 3 0 0 0 0-6zM6 21h12v2H6z',
}

export function KindIcon({ kind }: { kind: CardKind }) {
  return (
    <svg className="kind-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      <path d={KIND_ICON[kind]} />
    </svg>
  )
}

const MEANDER_UNITS = 12

const MEANDER_PATH = [
  `M0 9.4H${MEANDER_UNITS * 10}`,
  ...Array.from({ length: MEANDER_UNITS }, (_, index) => {
    const x = index * 10 + 1
    return `M${x} 9.4V1H${x + 7.5}V6.6H${x + 3}V3.6H${x + 5.2}`
  }),
].join('')

export function Meander({ className }: { className?: string }) {
  return (
    <svg className={className ? `meander ${className}` : 'meander'} viewBox={`0 0 ${MEANDER_UNITS * 10} 10`} aria-hidden="true" focusable="false">
      <path d={MEANDER_PATH} />
    </svg>
  )
}

export function Owl({ className }: { className?: string }) {
  return (
    <svg className={className ? `owl ${className}` : 'owl'} viewBox="0 0 64 72" aria-hidden="true" focusable="false">
      <path className="owl__body" d="M18 17L16 5L26 12.5A14 14 0 0 1 38 12.5L48 5L46 17A14 14 0 0 1 47 28C51 34 52 40 50 48C48 58 41 64 32 64C23 64 16 58 14 48C12 40 13 34 17 28A14 14 0 0 1 18 17Z" />
      <circle className="owl__eye" cx="25" cy="25" r="6.5" />
      <circle className="owl__eye" cx="39" cy="25" r="6.5" />
      <circle className="owl__pupil" cx="25" cy="25" r="2.6" />
      <circle className="owl__pupil" cx="39" cy="25" r="2.6" />
      <path className="owl__eye" d="M29.5 31L32 37L34.5 31Z" />
      <path className="owl__feathers" d="M24 43l4 3l4-3l4 3l4-3M22 50l5 3l5-3l5 3l5-3M25 57l3.5 2l3.5-2l3.5 2l3.5-2" />
      <path className="owl__feathers" d="M26 64v4M38 64v4M18 68.5h28" />
    </svg>
  )
}

export function cardImage(id: string, size: 'small' | 'large'): string {
  return `${SITE.base}cards/${id}${size === 'small' ? '-s' : ''}.webp`
}

function trackPointer(event: PointerEvent<HTMLDivElement>) {
  const element = event.currentTarget
  const box = element.getBoundingClientRect()
  const x = (event.clientX - box.left) / box.width
  const y = (event.clientY - box.top) / box.height
  element.style.setProperty('--mx', `${(x * 100).toFixed(1)}%`)
  element.style.setProperty('--my', `${(y * 100).toFixed(1)}%`)
  element.style.setProperty('--rx', `${((0.5 - y) * 14).toFixed(2)}deg`)
  element.style.setProperty('--ry', `${((x - 0.5) * 18).toFixed(2)}deg`)
  element.style.setProperty('--hover', '1')
}

const POINTER_PROPERTIES = ['--mx', '--my', '--rx', '--ry', '--hover']

function resetPointer(event: PointerEvent<HTMLDivElement>) {
  const element = event.currentTarget
  POINTER_PROPERTIES.forEach((name) => element.style.removeProperty(name))
}

export function HellasCard({ card, size = 'small', interactive = true }: { card: CardView; size?: 'small' | 'large'; interactive?: boolean }) {
  const pips = rank(card.rarity) + 1
  return (
    <div
      className={`rcard rcard--${card.rarity} rcard--${size} rcard--kind-${card.kind}`}
      onPointerMove={interactive ? trackPointer : undefined}
      onPointerLeave={interactive ? resetPointer : undefined}
    >
      <div className="rcard__frame">
        <div className="rcard__window">
          {card.art ? (
            <img
              className="rcard__art"
              src={cardImage(card.id, size)}
              alt=""
              loading="lazy"
              decoding="async"
              width={size === 'small' ? 320 : 640}
              height={size === 'small' ? 448 : 896}
            />
          ) : (
            <div className="rcard__placeholder">
              <Meander className="rcard__meander" />
              <KindIcon kind={card.kind} />
            </div>
          )}
          <div className="rcard__shade" />
        </div>
        <div className="rcard__top">
          <span className="rcard__kind">
            <KindIcon kind={card.kind} />
            {KIND_LABEL[card.kind].one}
          </span>
          <span className="rcard__pips" aria-label={RARITY_LABEL[card.rarity]}>
            {Array.from({ length: pips }, (_, index) => (
              <span key={index} className="rcard__pip" />
            ))}
          </span>
        </div>
        <div className="rcard__plate">
          <p className="rcard__name">{card.name}</p>
          <p className="rcard__subtitle">{frenchSpacing(card.subtitle)}</p>
          <p className="rcard__meta">
            <span>{RARITY_LABEL[card.rarity]}</span>
            <span aria-hidden="true">·</span>
            <span>{ERA_SHORT[card.era]}</span>
          </p>
        </div>
        <div className="rcard__foil" />
        <div className="rcard__glare" />
      </div>
    </div>
  )
}

export function CardBack({ rarity }: { rarity?: CardView['rarity'] }) {
  return (
    <div className={rarity ? `rcard rcard--back rcard--hint-${rarity}` : 'rcard rcard--back'}>
      <div className="rcard__frame">
        <div className="rcard__backface">
          <Meander className="rcard__meander" />
          <Owl className="rcard__owl" />
          <span className="rcard__emblem" aria-hidden="true">
            ΑΘΕ
          </span>
          <Meander className="rcard__meander rcard__meander--low" />
        </div>
      </div>
    </div>
  )
}
