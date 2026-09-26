[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-benchmark](../index.md) / AiBenchmarkJob

# Type Alias: AiBenchmarkJob

> **AiBenchmarkJob** = `object`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:59](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai-benchmark.ts#L59)

Server-side state of a user's background self-test run.

## Properties

### error?

> `optional` **error?**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:65](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai-benchmark.ts#L65)

Readable failure, when status is Failed.

***

### result?

> `optional` **result?**: [`AiBenchmarkResult`](AiBenchmarkResult.md)

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:63](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai-benchmark.ts#L63)

***

### startedAt?

> `optional` **startedAt?**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:62](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai-benchmark.ts#L62)

Epoch ms the run began; absent while idle.

***

### status

> **status**: [`AiBenchmarkJobStatus`](../enumerations/AiBenchmarkJobStatus.md)

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:60](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai-benchmark.ts#L60)
