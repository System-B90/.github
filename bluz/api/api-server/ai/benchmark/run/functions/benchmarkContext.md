[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/run](../index.md) / benchmarkContext

# Function: benchmarkContext()

> **benchmarkContext**(`actor`): [`AiToolContext`](../../../tools/types/type-aliases/AiToolContext.md)

Defined in: [ui/src/api-server/ai/benchmark/run.ts:67](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-server/ai/benchmark/run.ts#L67)

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
