[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/crypto](../index.md) / decryptSecret

# Function: decryptSecret()

> **decryptSecret**(`stored`): `string`

Defined in: [ui/src/api-server/crypto.ts:39](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-server/crypto.ts#L39)

Decrypts a value produced by [encryptSecret](encryptSecret.md). A value without the
`enc:v1:` prefix is returned unchanged — covers "" and any row written
before encryption was introduced.

## Parameters

### stored

`string`

## Returns

`string`
