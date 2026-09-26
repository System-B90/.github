[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/run](../index.md) / runAiBenchmark

# Function: runAiBenchmark()

> **runAiBenchmark**(`options`): `Promise`\<[`AiBenchmarkResult`](../../../../../api-shared/types/ai-benchmark/type-aliases/AiBenchmarkResult.md)\>

Defined in: [ui/src/api-server/ai/benchmark/run.ts:164](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/benchmark/run.ts#L164)

Runs the whole suite.

Cases run in sequence, not in parallel: a self-hosted gateway with one
worker — the deployment this feature exists for — answers four concurrent
turns by timing three of them out, which would report a perfectly good model
as broken.

## Parameters

### options

#### actor

\{ `displayName`: `string`; `id`: `string`; \}

#### actor.displayName

`string`

#### actor.id

`string`

#### provider

[`AiProvider`](../../../provider/type-aliases/AiProvider.md)

#### signal?

`AbortSignal`

## Returns

`Promise`\<[`AiBenchmarkResult`](../../../../../api-shared/types/ai-benchmark/type-aliases/AiBenchmarkResult.md)\>
