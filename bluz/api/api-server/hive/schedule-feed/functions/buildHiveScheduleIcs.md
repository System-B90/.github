[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/schedule-feed](../index.md) / buildHiveScheduleIcs

# Function: buildHiveScheduleIcs()

> **buildHiveScheduleIcs**(`events`, `lookup`, `options`): `string`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:111](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/hive/schedule-feed.ts#L111)

Renders events as Hive-loadable ICS. Pure: same input, same bytes, which
is what lets the route answer `If-None-Match` with a 304.

## Parameters

### events

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

Events to publish (hidden/archived are dropped here).

### lookup

[`HiveFeedLookup`](../type-aliases/HiveFeedLookup.md)

Hive name resolution for subjects, lessons, rooms, groups.

### options

[`HiveFeedOptions`](../type-aliases/HiveFeedOptions.md)

Category naming.

## Returns

`string`

The calendar text.
