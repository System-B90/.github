[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/iteration-request](../index.md) / resolveWritableIterationFromRequest

# Function: resolveWritableIterationFromRequest()

> **resolveWritableIterationFromRequest**(`request`): `Promise`\<[`ResolvedIteration`](../type-aliases/ResolvedIteration.md)\>

Defined in: [ui/src/api-server/iteration-request.ts:71](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/iteration-request.ts#L71)

Same as [resolveIterationFromRequest](resolveIterationFromRequest.md) but rejects writes to a past
(non-current) iteration. Use for POST/PUT/PATCH/DELETE handlers.
Uses a single DB lookup (existence + isCurrent check combined).

## Parameters

### request

`IterationRequestLike`

## Returns

`Promise`\<[`ResolvedIteration`](../type-aliases/ResolvedIteration.md)\>
