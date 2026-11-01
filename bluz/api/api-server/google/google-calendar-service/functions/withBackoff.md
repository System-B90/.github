[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / withBackoff

# Function: withBackoff()

> **withBackoff**\<`T`\>(`call`): `Promise`\<`T`\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:173](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/google/google-calendar-service.ts#L173)

Runs one Calendar API call with truncated exponential backoff + jitter.

## Type Parameters

### T

`T`

## Parameters

### call

() => `Promise`\<`T`\>

## Returns

`Promise`\<`T`\>
