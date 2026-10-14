[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-benchmark](../index.md) / AiBenchmarkJob

# Type Alias: AiBenchmarkJob

> **AiBenchmarkJob** = `object`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:118](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/ai-benchmark.ts#L118)

Server-side state of a user's background self-test run.

## Properties

### cases?

> `optional` **cases?**: [`AiBenchmarkLiveCase`](AiBenchmarkLiveCase.md)[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:124](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/ai-benchmark.ts#L124)

Per-case progress; present from the moment a run starts.

***

### error?

> `optional` **error?**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:126](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/ai-benchmark.ts#L126)

Readable failure, when status is Failed.

***

### result?

> `optional` **result?**: [`AiBenchmarkResult`](AiBenchmarkResult.md)

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:122](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/ai-benchmark.ts#L122)

***

### startedAt?

> `optional` **startedAt?**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:121](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/ai-benchmark.ts#L121)

Epoch ms the run began; absent while idle.

***

### status

> **status**: [`AiBenchmarkJobStatus`](../enumerations/AiBenchmarkJobStatus.md)

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:119](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/ai-benchmark.ts#L119)
