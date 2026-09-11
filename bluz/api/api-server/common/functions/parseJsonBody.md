[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / parseJsonBody

# Function: parseJsonBody()

> **parseJsonBody**\<`T`\>(`text`): `T`

Defined in: [ui/src/api-server/common.ts:34](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/common.ts#L34)

`JSON.parse` on a request body, with a malformed payload reported as the
400 it is. Parsing straight through leaks a `SyntaxError` into the generic
error handler, which answers an opaque 500 for what is a caller mistake.

## Type Parameters

### T

`T`

## Parameters

### text

`string`

## Returns

`T`
