[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/job](../index.md) / startBenchmarkJob

# Function: startBenchmarkJob()

> **startBenchmarkJob**(`options`): `object`

Defined in: [ui/src/api-server/ai/benchmark/job.ts:43](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/ai/benchmark/job.ts#L43)

Starts a run unless one is already going. Returns the job either way, so a
second click (or a second tab) just attaches to the run in flight.

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

## Returns

`object`

### job

> **job**: [`AiBenchmarkJob`](../../../../../api-shared/types/ai-benchmark/type-aliases/AiBenchmarkJob.md)

### started

> **started**: `boolean`
