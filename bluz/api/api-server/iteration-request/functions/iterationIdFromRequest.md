[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/iteration-request](../index.md) / iterationIdFromRequest

# Function: iterationIdFromRequest()

> **iterationIdFromRequest**(`request`): `string` \| `undefined`

Defined in: [ui/src/api-server/iteration-request.ts:46](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/iteration-request.ts#L46)

Read the `it` query param off a request. Absent or empty means the current
iteration (backward compatible with single-iteration callers).

## Parameters

### request

`IterationRequestLike`

## Returns

`string` \| `undefined`
