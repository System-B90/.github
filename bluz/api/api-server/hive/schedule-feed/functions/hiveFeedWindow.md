[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/schedule-feed](../index.md) / hiveFeedWindow

# Function: hiveFeedWindow()

> **hiveFeedWindow**(`now`, `hours`): `object`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:85](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/hive/schedule-feed.ts#L85)

The span the feed publishes: `hours` before the start of the current day
and `hours` after its end, the day taken in Israel time. The default 24
gives yesterday, today and tomorrow.

## Parameters

### now

`Date`

The moment the feed is built.

### hours

`number`

Hours on each side of today.

## Returns

`object`

The window's start and end.

### end

> **end**: `Date`

### start

> **start**: `Date`
