[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / toGoogleEventId

# Function: toGoogleEventId()

> **toGoogleEventId**(`bluzEventId`): `string`

Defined in: [ui/src/api-server/google/google-calendar-service.ts:280](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/google/google-calendar-service.ts#L280)

Deterministic, idempotent Google event id derived from the Bluz event id.
Bluz ids are mostly UUIDs / Mongo ObjectIds, so stripping dashes leaves
lowercase hex — a subset of the base32hex alphabet (a-v, 0-9) Google
requires. Any other id (the API takes client-supplied ones) is hex-encoded
instead, or Google would reject every push of that event.

## Parameters

### bluzEventId

`string`

## Returns

`string`
