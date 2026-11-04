[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/mongo-db-controller](../index.md) / StudentEngagementDocument

# Type Alias: StudentEngagementDocument

> **StudentEngagementDocument** = `object`

Defined in: [ui/src/api-server/mongo-db-controller.ts:455](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/mongo-db-controller.ts#L455)

One student's focused time on the schedule board for one day. `id` is
`<userId>:<date>` so the upsert is a single keyed `$inc` with no read.

## Properties

### date

> **date**: `string`

Defined in: [ui/src/api-server/mongo-db-controller.ts:459](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/mongo-db-controller.ts#L459)

`yyyy-MM-dd` in the app timezone.

***

### id

> **id**: `string`

Defined in: [ui/src/api-server/mongo-db-controller.ts:456](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/mongo-db-controller.ts#L456)

***

### ips?

> `optional` **ips?**: `string`[]

Defined in: [ui/src/api-server/mongo-db-controller.ts:464](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/mongo-db-controller.ts#L464)

Every address the board reported from that day (nginx-derived).

***

### seconds

> **seconds**: `number`

Defined in: [ui/src/api-server/mongo-db-controller.ts:461](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/mongo-db-controller.ts#L461)

Total seconds the board was open *and* focused that day.

***

### securityEventCount?

> `optional` **securityEventCount?**: `number`

Defined in: [ui/src/api-server/mongo-db-controller.ts:468](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/mongo-db-controller.ts#L468)

True total, including any dropped from `securityEvents`.

***

### securityEvents?

> `optional` **securityEvents?**: [`StudentSecurityEvent`](../../../api-shared/types/student-view/type-aliases/StudentSecurityEvent.md)[]

Defined in: [ui/src/api-server/mongo-db-controller.ts:466](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/mongo-db-controller.ts#L466)

Most recent suspected malicious attempts that day, oldest dropped first.

***

### updatedAt

> **updatedAt**: `Date`

Defined in: [ui/src/api-server/mongo-db-controller.ts:462](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/mongo-db-controller.ts#L462)

***

### userId

> **userId**: `string`

Defined in: [ui/src/api-server/mongo-db-controller.ts:457](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/mongo-db-controller.ts#L457)
