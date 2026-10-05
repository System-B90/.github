[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-reservations](../../../index.md) / [DbReservations](../index.md) / create

# Variable: create

> `const` **create**: (`reservation`, `controller`) => `Promise`\<[`DbReservation`](../../../../../api-shared/types/reservation/type-aliases/DbReservation.md)\> = `createReservation`

Defined in: [ui/src/api-server/db-reservations.ts:91](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/db-reservations.ts#L91)

## Parameters

### reservation

`Omit`\<[`DbReservation`](../../../../../api-shared/types/reservation/type-aliases/DbReservation.md), `"_id"`\>

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`DbReservation`](../../../../../api-shared/types/reservation/type-aliases/DbReservation.md)\>
