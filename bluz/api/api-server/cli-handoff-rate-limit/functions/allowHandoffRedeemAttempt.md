[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/cli-handoff-rate-limit](../index.md) / allowHandoffRedeemAttempt

# Function: allowHandoffRedeemAttempt()

> **allowHandoffRedeemAttempt**(`key`): `boolean`

Defined in: [ui/src/api-server/cli-handoff-rate-limit.ts:20](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/cli-handoff-rate-limit.ts#L20)

## Parameters

### key

`string`

## Returns

`boolean`

true when the caller is still under the limit (and records the hit).
