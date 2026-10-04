[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/iteration-query](../index.md) / withIteration

# Function: withIteration()

> **withIteration**(`endpoint`, `iterationId?`): `URL`

Defined in: [ui/src/api-client/iteration-query.ts:10](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-client/iteration-query.ts#L10)

Append the active iteration to a request, when one is selected. An absent id
means the current (writable) run, which every route treats as the default.

## Parameters

### endpoint

`URL`

### iterationId?

`string`

## Returns

`URL`
