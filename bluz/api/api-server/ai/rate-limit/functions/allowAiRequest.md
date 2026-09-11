[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/rate-limit](../index.md) / allowAiRequest

# Function: allowAiRequest()

> **allowAiRequest**(`userId`): `boolean`

Defined in: [ui/src/api-server/ai/rate-limit.ts:17](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/rate-limit.ts#L17)

## Parameters

### userId

`string`

## Returns

`boolean`

true when the caller is still under the limit (and records the hit).
