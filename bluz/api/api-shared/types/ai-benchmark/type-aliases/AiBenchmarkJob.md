[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-benchmark](../index.md) / AiBenchmarkJob

# Type Alias: AiBenchmarkJob

> **AiBenchmarkJob** = `object`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:108](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/ai-benchmark.ts#L108)

Server-side state of a user's background self-test run.

## Properties

### cases?

> `optional` **cases?**: [`AiBenchmarkLiveCase`](AiBenchmarkLiveCase.md)[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:114](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/ai-benchmark.ts#L114)

Per-case progress; present from the moment a run starts.

***

### error?

> `optional` **error?**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:116](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/ai-benchmark.ts#L116)

Readable failure, when status is Failed.

***

### result?

> `optional` **result?**: [`AiBenchmarkResult`](AiBenchmarkResult.md)

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:112](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/ai-benchmark.ts#L112)

***

### startedAt?

> `optional` **startedAt?**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:111](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/ai-benchmark.ts#L111)

Epoch ms the run began; absent while idle.

***

### status

> **status**: [`AiBenchmarkJobStatus`](../enumerations/AiBenchmarkJobStatus.md)

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:109](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/ai-benchmark.ts#L109)
