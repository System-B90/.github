[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/cli-handoff-rate-limit](../index.md) / allowHandoffRedeemAttempt

# Function: allowHandoffRedeemAttempt()

> **allowHandoffRedeemAttempt**(`key`): `boolean`

Defined in: [ui/src/api-server/cli-handoff-rate-limit.ts:20](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/cli-handoff-rate-limit.ts#L20)

## Parameters

### key

`string`

## Returns

`boolean`

true when the caller is still under the limit (and records the hit).
