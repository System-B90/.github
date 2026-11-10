[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/segments](../index.md) / spansMultipleDays

# Function: spansMultipleDays()

> **spansMultipleDays**(`start`, `end`): `boolean`

Defined in: [ui/src/components/schedule/calendar/split/segments.ts:229](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/schedule/calendar/split/segments.ts#L229)

Would a span starting at `start` and ending at `end` be drawn across more
than one local calendar day? Used to reject a drag/resize *before* it's
committed (#650), so bad spans are refused at the edit rather than merely
tolerated by the day-split fallback above.

## Parameters

### start

`number`

### end

`number`

## Returns

`boolean`
