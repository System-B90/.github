[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / pickFields

# Function: pickFields()

> **pickFields**\<`T`, `K`\>(`payload`, `fields`): `Pick`\<`T`, `K`\>

Defined in: [ui/src/api-server/common.ts:55](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/common.ts#L55)

Copy only the listed fields off a client-supplied payload.

Mongo creates used to persist the request body field-for-field, so a caller
could store arbitrary extra keys on a course/room/outsider/colour document -
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
