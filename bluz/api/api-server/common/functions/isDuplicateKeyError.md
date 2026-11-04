[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / isDuplicateKeyError

# Function: isDuplicateKeyError()

> **isDuplicateKeyError**(`e`): `boolean`

Defined in: [ui/src/api-server/common.ts:250](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/common.ts#L250)

A Mongo unique-index violation (error code 11000). Unlike the opaque
database errors below this one is entirely the caller's doing — it means the
id they supplied already exists — so it maps to 409, not 500 (#514).

## Parameters

### e

`unknown`

## Returns

`boolean`
