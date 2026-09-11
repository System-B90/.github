[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-room-extended-info](../../../index.md) / [DbRoomExtendedInfo](../index.md) / upsert

# Variable: upsert

> `const` **upsert**: (`roomId`, `roomSource`, `extendedInfo`, `controller`) => `Promise`\<`void`\> = `upsertExtendedInfo`

Defined in: [ui/src/api-server/db-room-extended-info.ts:48](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/db-room-extended-info.ts#L48)

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
