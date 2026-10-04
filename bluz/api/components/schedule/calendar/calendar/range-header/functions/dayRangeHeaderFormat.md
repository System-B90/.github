[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/range-header](../index.md) / dayRangeHeaderFormat

# Function: dayRangeHeaderFormat()

> **dayRangeHeaderFormat**(`__namedParameters`): `string`

Defined in: [ui/src/components/schedule/calendar/calendar/range-header.ts:11](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/schedule/calendar/calendar/range-header.ts#L11)

The calendar's week/day range header, e.g. `05 - 11 בספטמבר 2026`.

Kept out of CalendarView so the formatting -- in particular the bidi
isolation, which regresses silently and is invisible in code review -- can be
tested without mounting the calendar.

## Parameters

### \_\_namedParameters

#### end

`Date`

#### start

`Date`

## Returns

`string`
