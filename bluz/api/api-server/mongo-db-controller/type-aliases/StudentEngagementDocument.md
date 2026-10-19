[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/mongo-db-controller](../index.md) / StudentEngagementDocument

# Type Alias: StudentEngagementDocument

> **StudentEngagementDocument** = `object`

Defined in: [ui/src/api-server/mongo-db-controller.ts:419](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/mongo-db-controller.ts#L419)

One student's focused time on the schedule board for one day. `id` is
`<userId>:<date>` so the upsert is a single keyed `$inc` with no read.

## Properties

### date

> **date**: `string`

Defined in: [ui/src/api-server/mongo-db-controller.ts:423](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/mongo-db-controller.ts#L423)

`yyyy-MM-dd` in the app timezone.

***

### id

> **id**: `string`

Defined in: [ui/src/api-server/mongo-db-controller.ts:420](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/mongo-db-controller.ts#L420)

***

### seconds

> **seconds**: `number`

Defined in: [ui/src/api-server/mongo-db-controller.ts:425](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/mongo-db-controller.ts#L425)

Total seconds the board was open *and* focused that day.

***

### updatedAt

> **updatedAt**: `Date`

Defined in: [ui/src/api-server/mongo-db-controller.ts:426](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/mongo-db-controller.ts#L426)

***

### userId

> **userId**: `string`

Defined in: [ui/src/api-server/mongo-db-controller.ts:421](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/mongo-db-controller.ts#L421)
