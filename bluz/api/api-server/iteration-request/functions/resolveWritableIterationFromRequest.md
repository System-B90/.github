[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/iteration-request](../index.md) / resolveWritableIterationFromRequest

# Function: resolveWritableIterationFromRequest()

> **resolveWritableIterationFromRequest**(`request`): `Promise`\<[`ResolvedIteration`](../type-aliases/ResolvedIteration.md)\>

Defined in: [ui/src/api-server/iteration-request.ts:74](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/iteration-request.ts#L74)

Same as [resolveIterationFromRequest](resolveIterationFromRequest.md) but rejects writes to a past
(non-current) iteration. Use for POST/PUT/PATCH/DELETE handlers.
Uses a single DB lookup (existence + isCurrent check combined).

## Parameters

### request

`IterationRequestLike`

## Returns

`Promise`\<[`ResolvedIteration`](../type-aliases/ResolvedIteration.md)\>
