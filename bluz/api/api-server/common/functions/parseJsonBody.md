[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / parseJsonBody

# Function: parseJsonBody()

> **parseJsonBody**\<`T`\>(`text`): `T`

Defined in: [ui/src/api-server/common.ts:40](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-server/common.ts#L40)

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
