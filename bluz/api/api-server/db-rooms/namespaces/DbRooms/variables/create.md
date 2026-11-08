[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-rooms](../../../index.md) / [DbRooms](../index.md) / create

# Variable: create

> `const` **create**: (`room`, `controller`) => `Promise`\<`Pick`\<[`CustomRoom`](../../../../../api-shared/types/room/type-aliases/CustomRoom.md), `"id"` \| `"name"` \| `"source"` \| `"description"` \| `"extendedInfo"`\>\> = `createDbRoom`

Defined in: [ui/src/api-server/db-rooms.ts:86](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/db-rooms.ts#L86)

## Parameters

### room

[`CustomRoom`](../../../../../api-shared/types/room/type-aliases/CustomRoom.md)

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<`Pick`\<[`CustomRoom`](../../../../../api-shared/types/room/type-aliases/CustomRoom.md), `"id"` \| `"name"` \| `"source"` \| `"description"` \| `"extendedInfo"`\>\>
