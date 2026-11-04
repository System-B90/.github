[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-rooms](../../../index.md) / [DbRooms](../index.md) / create

# Variable: create

> `const` **create**: (`room`, `controller`) => `Promise`\<`Pick`\<[`CustomRoom`](../../../../../api-shared/types/room/type-aliases/CustomRoom.md), `"id"` \| `"name"` \| `"source"` \| `"description"` \| `"extendedInfo"`\>\> = `createDbRoom`

Defined in: [ui/src/api-server/db-rooms.ts:86](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/db-rooms.ts#L86)

## Parameters

### room

[`CustomRoom`](../../../../../api-shared/types/room/type-aliases/CustomRoom.md)

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<`Pick`\<[`CustomRoom`](../../../../../api-shared/types/room/type-aliases/CustomRoom.md), `"id"` \| `"name"` \| `"source"` \| `"description"` \| `"extendedInfo"`\>\>
