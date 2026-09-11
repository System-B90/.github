[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/segments](../index.md) / splitAtDayBoundaries

# Function: splitAtDayBoundaries()

> **splitAtDayBoundaries**(`start`, `end`): `object`[]

Defined in: [ui/src/components/schedule/calendar/split/segments.ts:109](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/split/segments.ts#L109)

react-big-calendar lays each event out in exactly one day column; a piece
whose wall-clock span crosses local midnight has no such column and gets
silently dropped from the grid (#650). The drag handler in CalendarView
refuses to *create* such a span, but nothing stops one from already
existing in stored data (a pre-fix event, an import, a direct API write) —
so this is the last line of defence: any piece still crossing a day
boundary is cut at midnight into day-local pieces before it ever reaches
react-big-calendar, so the worst case is a visibly truncated block, never
an invisible one.

## Parameters

### start

`number`

### end

`number`

## Returns

`object`[]
