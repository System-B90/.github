[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/run](../index.md) / benchmarkContext

# Function: benchmarkContext()

> **benchmarkContext**(`actor`): [`AiToolContext`](../../../tools/types/type-aliases/AiToolContext.md)

Defined in: [ui/src/api-server/ai/benchmark/run.ts:76](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/ai/benchmark/run.ts#L76)

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
