[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-reservations](../../../index.md) / [DbReservations](../index.md) / create

# Variable: create

> `const` **create**: (`reservation`, `controller`) => `Promise`\<[`DbReservation`](../../../../../api-shared/types/reservation/type-aliases/DbReservation.md)\> = `createReservation`

Defined in: [ui/src/api-server/db-reservations.ts:100](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/db-reservations.ts#L100)

## Parameters

### reservation

`Omit`\<[`DbReservation`](../../../../../api-shared/types/reservation/type-aliases/DbReservation.md), `"_id"`\>

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`DbReservation`](../../../../../api-shared/types/reservation/type-aliases/DbReservation.md)\>
