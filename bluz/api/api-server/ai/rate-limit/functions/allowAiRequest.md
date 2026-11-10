[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/rate-limit](../index.md) / allowAiRequest

# Function: allowAiRequest()

> **allowAiRequest**(`userId`): `boolean`

Defined in: [ui/src/api-server/ai/rate-limit.ts:19](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/ai/rate-limit.ts#L19)

## Parameters

### userId

`string`

## Returns

`boolean`

true when the caller is still under the limit (and records the hit).
