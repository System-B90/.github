[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/app-day](../index.md) / nextAppMidnight

# Function: nextAppMidnight()

> **nextAppMidnight**(`instant`): `Date`

Defined in: [ui/src/api-shared/app-day.ts:24](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/app-day.ts#L24)

The instant the app-timezone day containing `instant` ends — the next
Jerusalem midnight. Stepped by civil date, not by adding 24h, so a DST
transition day (23h / 25h) still ends at 00:00: 36h past any midnight is
always inside the next day.

## Parameters

### instant

`number` \| `Date`

## Returns

`Date`
