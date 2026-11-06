[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/iteration-request](../index.md) / resolveWritableIterationFromRequest

# Function: resolveWritableIterationFromRequest()

> **resolveWritableIterationFromRequest**(`request`): `Promise`\<[`ResolvedIteration`](../type-aliases/ResolvedIteration.md)\>

Defined in: [ui/src/api-server/iteration-request.ts:74](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/iteration-request.ts#L74)

Same as [resolveIterationFromRequest](resolveIterationFromRequest.md) but rejects writes to a past
(non-current) iteration. Use for POST/PUT/PATCH/DELETE handlers.
Uses a single DB lookup (existence + isCurrent check combined).

## Parameters

### request

`IterationRequestLike`

## Returns

`Promise`\<[`ResolvedIteration`](../type-aliases/ResolvedIteration.md)\>
