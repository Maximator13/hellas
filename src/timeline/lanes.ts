import type { HistoricalEvent, Track, TrackId } from '../data/schema.ts'
import { estimateLabelWidth, isVisibleAt, placeLabels } from './layout.ts'
import { xToYear, yearToX, type Viewport } from './viewport.ts'

export const MAIN_ROWS = 3
export const MAX_SECONDARY_LANES = 4

export interface TrackSegment {
  id: string
  name: string
  color: string
  from: number
  to: number
}

export interface PlacedEvent {
  event: HistoricalEvent
  color: string
  x: number
  endX: number | null
  row: number | null
}

export interface LaneLayout {
  lane: number
  rows: number
  segments: TrackSegment[]
  events: PlacedEvent[]
}

type Interval = [number, number]

function visibleSpans(track: Track, from: number, to: number): Interval[] {
  return track.spans
    .filter((span) => span.end >= from && span.start <= to)
    .map((span): Interval => [Math.max(span.start, from), Math.min(span.end, to)])
}

function collides(taken: Interval[], wanted: Interval[], gap: number): boolean {
  return wanted.some(([start, end]) => taken.some(([from, to]) => start < to + gap && end + gap > from))
}

export function assignLanes(tracks: Track[], from: number, to: number, gap = 0): Map<TrackId, number> {
  const lanes = new Map<TrackId, number>()
  const [main, ...others] = tracks
  if (main) lanes.set(main.id, 0)
  const taken: Interval[][] = []
  for (const track of others) {
    const wanted = visibleSpans(track, from, to)
    if (wanted.length === 0) continue
    let row = taken.findIndex((intervals) => !collides(intervals, wanted, gap))
    if (row < 0 && taken.length < MAX_SECONDARY_LANES) row = taken.push([]) - 1
    if (row < 0) continue
    taken[row]!.push(...wanted)
    lanes.set(track.id, row + 1)
  }
  return lanes
}

export function layoutLanes(
  view: Viewport,
  width: number,
  tracks: Track[],
  events: HistoricalEvent[],
  selectedId: string | null,
): LaneLayout[] {
  const viewStart = xToYear(0, view, width)
  const viewEnd = xToYear(width, view, width)
  const labelReach = view.span * 0.15
  const visibleCount = new Map<TrackId, number>()
  for (const event of events) {
    if (event.start > viewEnd || (event.end ?? event.start) < viewStart || !isVisibleAt(event.importance, view.span)) continue
    visibleCount.set(event.track, (visibleCount.get(event.track) ?? 0) + 1)
  }
  const [main, ...others] = tracks
  const ranked = main ? [main, ...others.toSorted((a, b) => (visibleCount.get(b.id) ?? 0) - (visibleCount.get(a.id) ?? 0))] : []
  const lanes = assignLanes(ranked, viewStart, viewEnd, view.span * 0.08)
  const colors = new Map(tracks.map((track) => [track.id, track.color]))
  const laneCount = Math.max(0, ...lanes.values()) + 1
  return Array.from({ length: laneCount }, (_, lane) => {
    const rows = lane === 0 ? MAIN_ROWS : 1
    const segments = tracks
      .filter((track) => lanes.get(track.id) === lane)
      .flatMap((track) =>
        visibleSpans(track, viewStart, viewEnd).map(([start, end]) => ({
          id: `${track.id}-${start}`,
          name: track.name,
          color: track.color,
          from: yearToX(start, view, width),
          to: yearToX(end, view, width),
        })),
      )
    const shown = events.filter(
      (event) =>
        (lanes.get(event.track) ?? 0) === lane &&
        (isVisibleAt(event.importance, view.span) || event.id === selectedId) &&
        (event.end ?? event.start) >= viewStart - labelReach &&
        event.start <= viewEnd,
    )
    const candidates = shown.map((event) => ({
      id: event.id,
      x: yearToX(event.start, view, width),
      width: estimateLabelWidth(event.title),
      importance: event.id === selectedId ? (1 as const) : event.importance,
      start: event.start,
    }))
    const slots = new Map(placeLabels(candidates, rows).map((slot) => [slot.id, slot.row]))
    const placed = shown.map((event) => ({
      event,
      color: colors.get(event.track) ?? '',
      x: yearToX(event.start, view, width),
      endX: event.end !== undefined && event.end > event.start ? yearToX(event.end, view, width) : null,
      row: slots.get(event.id) ?? null,
    }))
    return { lane, rows, segments, events: placed }
  })
}
