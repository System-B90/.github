[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/segments](../index.md) / buildEventSegments

# Function: buildEventSegments()

> **buildEventSegments**(`events`, `windows?`): [`EventSegment`](../type-aliases/EventSegment.md)[]

Defined in: [ui/src/components/schedule/calendar/split/segments.ts:74](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/split/segments.ts#L74)

Expands every event into its drawn pieces.

## Parameters

### events

readonly [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

The complete event set — breaks are harvested from it, so a
              range- or filter-narrowed subset would silently change how
              events split.

### windows?

readonly [`BreakWindow`](../../../../../../api-shared/break-windows/type-aliases/BreakWindow.md)[] = `...`

Break windows, when the caller already has them.

## Returns

[`EventSegment`](../type-aliases/EventSegment.md)[]

Segments in event order, each tagged with its position.
