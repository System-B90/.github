[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/segments](../index.md) / spansMultipleDays

# Function: spansMultipleDays()

> **spansMultipleDays**(`start`, `end`): `boolean`

Defined in: [ui/src/components/schedule/calendar/split/segments.ts:229](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/schedule/calendar/split/segments.ts#L229)

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
