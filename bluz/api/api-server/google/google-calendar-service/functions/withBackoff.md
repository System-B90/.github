[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / withBackoff

# Function: withBackoff()

> **withBackoff**\<`T`\>(`call`): `Promise`\<`T`\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:173](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/google/google-calendar-service.ts#L173)

Runs one Calendar API call with truncated exponential backoff + jitter.

## Type Parameters

### T

`T`

## Parameters

### call

() => `Promise`\<`T`\>

## Returns

`Promise`\<`T`\>
