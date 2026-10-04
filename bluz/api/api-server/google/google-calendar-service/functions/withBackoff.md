[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / withBackoff

# Function: withBackoff()

> **withBackoff**\<`T`\>(`call`): `Promise`\<`T`\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:153](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/google/google-calendar-service.ts#L153)

Runs one Calendar API call with truncated exponential backoff + jitter.

## Type Parameters

### T

`T`

## Parameters

### call

() => `Promise`\<`T`\>

## Returns

`Promise`\<`T`\>
