[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / parseJsonBody

# Function: parseJsonBody()

> **parseJsonBody**\<`T`\>(`text`): `T`

Defined in: [ui/src/api-server/common.ts:42](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/common.ts#L42)

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
