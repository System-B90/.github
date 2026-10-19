[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-dialog/TimeFields](../index.md) / isEndTimeValid

# Function: isEndTimeValid()

> **isEndTimeValid**(`startTime`, `endTime`): `boolean`

Defined in: [ui/src/components/schedule/event-dialog/TimeFields.tsx:24](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/event-dialog/TimeFields.tsx#L24)

Whether an end time may be written back for a given start.

An end at or before the start is a negative duration. Accepting one cached
that duration and carried the corruption into later start-time edits, where
a `Math.max(0, …)` downstream merely hid it (#623).

## Parameters

### startTime

`Dayjs` \| `null` \| `undefined`

The event's current start, if it has one.

### endTime

`Dayjs`

The end the user just picked.

## Returns

`boolean`
