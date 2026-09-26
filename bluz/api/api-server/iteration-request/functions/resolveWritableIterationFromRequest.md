[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/iteration-request](../index.md) / resolveWritableIterationFromRequest

# Function: resolveWritableIterationFromRequest()

> **resolveWritableIterationFromRequest**(`request`): `Promise`\<[`ResolvedIteration`](../type-aliases/ResolvedIteration.md)\>

Defined in: [ui/src/api-server/iteration-request.ts:71](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/iteration-request.ts#L71)

Same as [resolveIterationFromRequest](resolveIterationFromRequest.md) but rejects writes to a past
(non-current) iteration. Use for POST/PUT/PATCH/DELETE handlers.
Uses a single DB lookup (existence + isCurrent check combined).

## Parameters

### request

`IterationRequestLike`

## Returns

`Promise`\<[`ResolvedIteration`](../type-aliases/ResolvedIteration.md)\>
