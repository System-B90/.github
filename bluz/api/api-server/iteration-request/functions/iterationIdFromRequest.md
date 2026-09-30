[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/iteration-request](../index.md) / iterationIdFromRequest

# Function: iterationIdFromRequest()

> **iterationIdFromRequest**(`request`): `string` \| `undefined`

Defined in: [ui/src/api-server/iteration-request.ts:45](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/iteration-request.ts#L45)

Read the `it` query param off a request. Absent or empty means the current
iteration (backward compatible with single-iteration callers).

## Parameters

### request

`IterationRequestLike`

## Returns

`string` \| `undefined`
