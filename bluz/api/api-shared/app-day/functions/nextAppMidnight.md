[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/app-day](../index.md) / nextAppMidnight

# Function: nextAppMidnight()

> **nextAppMidnight**(`instant`): `Date`

Defined in: [ui/src/api-shared/app-day.ts:24](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/app-day.ts#L24)

The instant the app-timezone day containing `instant` ends — the next
Jerusalem midnight. Stepped by civil date, not by adding 24h, so a DST
transition day (23h / 25h) still ends at 00:00: 36h past any midnight is
always inside the next day.

## Parameters

### instant

`number` \| `Date`

## Returns

`Date`
