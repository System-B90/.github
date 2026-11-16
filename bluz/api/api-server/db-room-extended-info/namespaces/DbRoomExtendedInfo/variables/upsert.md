[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-room-extended-info](../../../index.md) / [DbRoomExtendedInfo](../index.md) / upsert

# Variable: upsert

> `const` **upsert**: (`roomId`, `roomSource`, `extendedInfo`, `controller`) => `Promise`\<`void`\> = `upsertExtendedInfo`

Defined in: [ui/src/api-server/db-room-extended-info.ts:62](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/api-server/db-room-extended-info.ts#L62)

## Parameters

### roomId

[`RoomId`](../../../../../api-shared/types/room/type-aliases/RoomId.md)

### roomSource

[`RoomSource`](../../../../../api-shared/types/room/enumerations/RoomSource.md)

### extendedInfo

[`RoomExtendedInfo`](../../../../../api-shared/types/room/type-aliases/RoomExtendedInfo.md)

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<`void`\>
