[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / pickFields

# Function: pickFields()

> **pickFields**\<`T`, `K`\>(`payload`, `fields`): `Pick`\<`T`, `K`\>

Defined in: [ui/src/api-server/common.ts:60](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/common.ts#L60)

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
