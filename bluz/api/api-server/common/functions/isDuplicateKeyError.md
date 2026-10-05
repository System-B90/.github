[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / isDuplicateKeyError

# Function: isDuplicateKeyError()

> **isDuplicateKeyError**(`e`): `boolean`

Defined in: [ui/src/api-server/common.ts:216](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/common.ts#L216)

A Mongo unique-index violation (error code 11000). Unlike the opaque
database errors below this one is entirely the caller's doing — it means the
id they supplied already exists — so it maps to 409, not 500 (#514).

## Parameters

### e

`unknown`

## Returns

`boolean`
