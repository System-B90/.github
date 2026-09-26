[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-module-event](../index.md) / assignShuffleGroupMembers

# Function: assignShuffleGroupMembers()

> **assignShuffleGroupMembers**\<`T`\>(`existing`, `wanted`, `originId`): `object`

Defined in: [ui/src/api-server/gantt/db-module-event.ts:230](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-module-event.ts#L230)

Decides which existing group member keeps which of the `wanted` shuffles.

A member that already carries a wanted name keeps it. An untagged (or stale)
member takes the next free name instead of being deleted - otherwise grouping
an ungrouped event would throw away the very event the user grouped, along
with its placement. The origin is offered a free name before any sibling:
it is the event whose dialog the user is editing, so losing it to a sibling
would delete the event out from under the open dialog.

Returns the claimed members by name and the members left without one.

## Type Parameters

### T

`T` *extends* `object`

## Parameters

### existing

`T`[]

### wanted

`string`[]

### originId

`string`

## Returns

`object`

### claimed

> **claimed**: `Map`\<`string`, `T`\>

### orphans

> **orphans**: `T`[]
