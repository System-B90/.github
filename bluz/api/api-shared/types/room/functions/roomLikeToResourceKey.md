[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/room](../index.md) / roomLikeToResourceKey

# Function: roomLikeToResourceKey()

> **roomLikeToResourceKey**(`room`): `string`

Defined in: [ui/src/api-shared/types/room.ts:83](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/room.ts#L83)

Stable composite key for matching a room across the calendar resource layer
(react-big-calendar `resourceIdAccessor` / `resourceAccessor`). Uses a `:`
separator so the key round-trips unambiguously even when the room id itself
contains `-` (custom-room UUIDs, the "no-room" sentinel). Replaces the old
`JSON.stringify(room)` matching, which was fragile to property order / extra
fields and could silently drop events into the "no room" column (#170).

This is the only room-key format in the codebase. The legacy
`${source}-${id}` format it once coexisted with (#544/17) was retired:
its last consumers — the extended-info join in `app/api/rooms/utils.ts`,
two cosmetic React keys, and an unconsumed WS broadcast key — all derived
the string in memory from structured data (the persisted
`DbRoomExtendedInfo` documents store roomId/roomSource as separate
fields), so cutting them over needed no data backfill.

## Parameters

### room

[`RoomLike`](../type-aliases/RoomLike.md)

## Returns

`string`
