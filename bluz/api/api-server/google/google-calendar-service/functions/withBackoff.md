[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / withBackoff

# Function: withBackoff()

> **withBackoff**\<`T`\>(`call`): `Promise`\<`T`\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:173](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/google/google-calendar-service.ts#L173)

Runs one Calendar API call with truncated exponential backoff + jitter.

## Type Parameters

### T

`T`

## Parameters

### call

() => `Promise`\<`T`\>

## Returns

`Promise`\<`T`\>
