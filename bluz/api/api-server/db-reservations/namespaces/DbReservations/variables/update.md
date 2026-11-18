[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-reservations](../../../index.md) / [DbReservations](../index.md) / update

# Variable: update

> `const` **update**: (`reservationId`, `fields`, `controller`) => `Promise`\<[`DbReservation`](../../../../../api-shared/types/reservation/type-aliases/DbReservation.md)\> = `updateReservation`

Defined in: [ui/src/api-server/db-reservations.ts:157](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-server/db-reservations.ts#L157)

## Parameters

### reservationId

`string`

### fields

`Omit`\<[`DbReservation`](../../../../../api-shared/types/reservation/type-aliases/DbReservation.md), `"_id"` \| `"createdBy"`\>

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`DbReservation`](../../../../../api-shared/types/reservation/type-aliases/DbReservation.md)\>
