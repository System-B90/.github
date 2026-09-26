[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/run](../index.md) / benchmarkContext

# Function: benchmarkContext()

> **benchmarkContext**(`actor`): [`AiToolContext`](../../../tools/types/type-aliases/AiToolContext.md)

Defined in: [ui/src/api-server/ai/benchmark/run.ts:42](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/benchmark/run.ts#L42)

The context handed to fixture tools.

The controller factories throw rather than returning a stub: no fixture tool
asks for one, and if one ever did, failing loudly is the only acceptable
outcome — a self-test that quietly reaches the user's real database is worse
than no self-test.

## Parameters

### actor

#### displayName

`string`

#### id

`string`

## Returns

[`AiToolContext`](../../../tools/types/type-aliases/AiToolContext.md)
