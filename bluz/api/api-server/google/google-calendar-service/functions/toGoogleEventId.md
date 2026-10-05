[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / toGoogleEventId

# Function: toGoogleEventId()

> **toGoogleEventId**(`bluzEventId`): `string`

Defined in: [ui/src/api-server/google/google-calendar-service.ts:243](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/google/google-calendar-service.ts#L243)

Deterministic, idempotent Google event id derived from the Bluz event id.
Bluz ids are UUIDs / Mongo ObjectIds, so stripping dashes leaves lowercase
hex — a subset of the base32hex alphabet (a-v, 0-9) Google requires.

## Parameters

### bluzEventId

`string`

## Returns

`string`
