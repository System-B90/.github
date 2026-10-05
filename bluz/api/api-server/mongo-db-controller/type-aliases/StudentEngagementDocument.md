[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/mongo-db-controller](../index.md) / StudentEngagementDocument

# Type Alias: StudentEngagementDocument

> **StudentEngagementDocument** = `object`

Defined in: [ui/src/api-server/mongo-db-controller.ts:396](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/mongo-db-controller.ts#L396)

One student's focused time on the schedule board for one day. `id` is
`<userId>:<date>` so the upsert is a single keyed `$inc` with no read.

## Properties

### date

> **date**: `string`

Defined in: [ui/src/api-server/mongo-db-controller.ts:400](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/mongo-db-controller.ts#L400)

`yyyy-MM-dd` in the app timezone.

***

### id

> **id**: `string`

Defined in: [ui/src/api-server/mongo-db-controller.ts:397](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/mongo-db-controller.ts#L397)

***

### seconds

> **seconds**: `number`

Defined in: [ui/src/api-server/mongo-db-controller.ts:402](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/mongo-db-controller.ts#L402)

Total seconds the board was open *and* focused that day.

***

### updatedAt

> **updatedAt**: `Date`

Defined in: [ui/src/api-server/mongo-db-controller.ts:403](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/mongo-db-controller.ts#L403)

***

### userId

> **userId**: `string`

Defined in: [ui/src/api-server/mongo-db-controller.ts:398](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/mongo-db-controller.ts#L398)
