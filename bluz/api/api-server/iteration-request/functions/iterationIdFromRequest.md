[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/iteration-request](../index.md) / iterationIdFromRequest

# Function: iterationIdFromRequest()

> **iterationIdFromRequest**(`request`): `string` \| `undefined`

Defined in: [ui/src/api-server/iteration-request.ts:46](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-server/iteration-request.ts#L46)

Read the `it` query param off a request. Absent or empty means the current
iteration (backward compatible with single-iteration callers).

## Parameters

### request

`IterationRequestLike`

## Returns

`string` \| `undefined`
