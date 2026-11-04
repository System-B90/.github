[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/rate-limit](../index.md) / allowAiRequest

# Function: allowAiRequest()

> **allowAiRequest**(`userId`): `boolean`

Defined in: [ui/src/api-server/ai/rate-limit.ts:19](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/ai/rate-limit.ts#L19)

## Parameters

### userId

`string`

## Returns

`boolean`

true when the caller is still under the limit (and records the hit).
