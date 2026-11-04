[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/iteration-request](../index.md) / iterationIdFromRequest

# Function: iterationIdFromRequest()

> **iterationIdFromRequest**(`request`): `string` \| `undefined`

Defined in: [ui/src/api-server/iteration-request.ts:46](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/iteration-request.ts#L46)

Read the `it` query param off a request. Absent or empty means the current
iteration (backward compatible with single-iteration callers).

## Parameters

### request

`IterationRequestLike`

## Returns

`string` \| `undefined`
