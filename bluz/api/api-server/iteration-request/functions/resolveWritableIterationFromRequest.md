[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/iteration-request](../index.md) / resolveWritableIterationFromRequest

# Function: resolveWritableIterationFromRequest()

> **resolveWritableIterationFromRequest**(`request`): `Promise`\<[`ResolvedIteration`](../type-aliases/ResolvedIteration.md)\>

Defined in: [ui/src/api-server/iteration-request.ts:71](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/iteration-request.ts#L71)

Same as [resolveIterationFromRequest](resolveIterationFromRequest.md) but rejects writes to a past
(non-current) iteration. Use for POST/PUT/PATCH/DELETE handlers.
Uses a single DB lookup (existence + isCurrent check combined).

## Parameters

### request

`IterationRequestLike`

## Returns

`Promise`\<[`ResolvedIteration`](../type-aliases/ResolvedIteration.md)\>
