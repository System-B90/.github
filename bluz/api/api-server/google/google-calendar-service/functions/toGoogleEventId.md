[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / toGoogleEventId

# Function: toGoogleEventId()

> **toGoogleEventId**(`bluzEventId`): `string`

Defined in: [ui/src/api-server/google/google-calendar-service.ts:280](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/google/google-calendar-service.ts#L280)

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
