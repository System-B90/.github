[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / toGoogleEventId

# Function: toGoogleEventId()

> **toGoogleEventId**(`bluzEventId`): `string`

Defined in: [ui/src/api-server/google/google-calendar-service.ts:258](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/google/google-calendar-service.ts#L258)

Deterministic, idempotent Google event id derived from the Bluz event id.
Bluz ids are UUIDs / Mongo ObjectIds, so stripping dashes leaves lowercase
hex — a subset of the base32hex alphabet (a-v, 0-9) Google requires.

## Parameters

### bluzEventId

`string`

## Returns

`string`
