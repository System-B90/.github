[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-reservations](../../../index.md) / [DbReservations](../index.md) / get

# Variable: get

> `const` **get**: (`roomId?`, `roomSource?`, `from?`, `to?`, `controller`) => `Promise`\<[`DbReservation`](../../../../../api-shared/types/reservation/type-aliases/DbReservation.md)[]\> = `getReservations`

Defined in: [ui/src/api-server/db-reservations.ts:155](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-server/db-reservations.ts#L155)

## Parameters

### roomId?

[`RoomId`](../../../../../api-shared/types/room/type-aliases/RoomId.md)

### roomSource?

[`RoomSource`](../../../../../api-shared/types/room/enumerations/RoomSource.md)

### from?

`string`

### to?

`string`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`DbReservation`](../../../../../api-shared/types/reservation/type-aliases/DbReservation.md)[]\>
