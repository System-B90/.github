[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / withBackoff

# Function: withBackoff()

> **withBackoff**\<`T`\>(`call`): `Promise`\<`T`\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:173](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/google/google-calendar-service.ts#L173)

Runs one Calendar API call with truncated exponential backoff + jitter.

## Type Parameters

### T

`T`

## Parameters

### call

() => `Promise`\<`T`\>

## Returns

`Promise`\<`T`\>
