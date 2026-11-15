[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-reservations](../../../index.md) / [DbReservations](../index.md) / update

# Variable: update

> `const` **update**: (`reservationId`, `fields`, `controller`) => `Promise`\<[`DbReservation`](../../../../../api-shared/types/reservation/type-aliases/DbReservation.md)\> = `updateReservation`

Defined in: [ui/src/api-server/db-reservations.ts:157](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/db-reservations.ts#L157)

## Parameters

### reservationId

`string`

### fields

`Omit`\<[`DbReservation`](../../../../../api-shared/types/reservation/type-aliases/DbReservation.md), `"_id"` \| `"createdBy"`\>

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`DbReservation`](../../../../../api-shared/types/reservation/type-aliases/DbReservation.md)\>
