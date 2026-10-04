[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/run](../index.md) / runAiBenchmark

# Function: runAiBenchmark()

> **runAiBenchmark**(`options`): `Promise`\<[`AiBenchmarkResult`](../../../../../api-shared/types/ai-benchmark/type-aliases/AiBenchmarkResult.md)\>

Defined in: [ui/src/api-server/ai/benchmark/run.ts:222](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/benchmark/run.ts#L222)

Runs the whole suite.

Cases run in sequence, not in parallel: a self-hosted gateway with one
worker — the deployment this feature exists for — answers concurrent turns
by timing most of them out, which would report a perfectly good model as
broken.

`onProgress` gets a fresh snapshot after every state change, for the live
view.

## Parameters

### options

#### actor

\{ `displayName`: `string`; `id`: `string`; \}

#### actor.displayName

`string`

#### actor.id

`string`

#### onProgress?

(`cases`) => `void`

#### provider

[`AiProvider`](../../../provider/type-aliases/AiProvider.md)

#### signal?

`AbortSignal`

## Returns

`Promise`\<[`AiBenchmarkResult`](../../../../../api-shared/types/ai-benchmark/type-aliases/AiBenchmarkResult.md)\>
