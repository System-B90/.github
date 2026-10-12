[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/rate-limit](../index.md) / allowAiRequest

# Function: allowAiRequest()

> **allowAiRequest**(`userId`): `boolean`

Defined in: [ui/src/api-server/ai/rate-limit.ts:19](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-server/ai/rate-limit.ts#L19)

## Parameters

### userId

`string`

## Returns

`boolean`

true when the caller is still under the limit (and records the hit).
