[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/cli-handoff-rate-limit](../index.md) / allowHandoffRedeemAttempt

# Function: allowHandoffRedeemAttempt()

> **allowHandoffRedeemAttempt**(`key`): `boolean`

Defined in: [ui/src/api-server/cli-handoff-rate-limit.ts:20](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/cli-handoff-rate-limit.ts#L20)

## Parameters

### key

`string`

## Returns

`boolean`

true when the caller is still under the limit (and records the hit).
