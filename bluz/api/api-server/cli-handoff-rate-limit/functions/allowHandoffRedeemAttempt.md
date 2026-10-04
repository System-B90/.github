[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/cli-handoff-rate-limit](../index.md) / allowHandoffRedeemAttempt

# Function: allowHandoffRedeemAttempt()

> **allowHandoffRedeemAttempt**(`key`): `boolean`

Defined in: [ui/src/api-server/cli-handoff-rate-limit.ts:20](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/cli-handoff-rate-limit.ts#L20)

## Parameters

### key

`string`

## Returns

`boolean`

true when the caller is still under the limit (and records the hit).
