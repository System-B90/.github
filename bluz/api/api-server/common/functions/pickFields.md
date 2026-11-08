[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / pickFields

# Function: pickFields()

> **pickFields**\<`T`, `K`\>(`payload`, `fields`): `Pick`\<`T`, `K`\>

Defined in: [ui/src/api-server/common.ts:66](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/common.ts#L66)

Copy only the listed fields off a client-supplied payload.

Mongo creates used to persist the request body field-for-field, so a caller
could store arbitrary extra keys on a course/room/outsider/color document -
including `_id`, which then fights the driver - and any field the app later
gives meaning to was retroactively client-writable (#538 item 4). Postgres
writes get this from `sanitizeCreatePayload`; this is the Mongo counterpart.

Absent keys stay absent rather than becoming `undefined` values, so an
optional field is not stored as a null-ish key.

## Type Parameters

### T

`T` *extends* `object`

### K

`K` *extends* `string` \| `number` \| `symbol`

## Parameters

### payload

`T`

### fields

readonly `K`[]

## Returns

`Pick`\<`T`, `K`\>
