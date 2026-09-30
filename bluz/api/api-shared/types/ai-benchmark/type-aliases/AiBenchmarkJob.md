[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-benchmark](../index.md) / AiBenchmarkJob

# Type Alias: AiBenchmarkJob

> **AiBenchmarkJob** = `object`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:103](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L103)

Server-side state of a user's background self-test run.

## Properties

### cases?

> `optional` **cases?**: [`AiBenchmarkLiveCase`](AiBenchmarkLiveCase.md)[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:109](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L109)

Per-case progress; present from the moment a run starts.

***

### error?

> `optional` **error?**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:111](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L111)

Readable failure, when status is Failed.

***

### result?

> `optional` **result?**: [`AiBenchmarkResult`](AiBenchmarkResult.md)

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:107](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L107)

***

### startedAt?

> `optional` **startedAt?**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:106](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L106)

Epoch ms the run began; absent while idle.

***

### status

> **status**: [`AiBenchmarkJobStatus`](../enumerations/AiBenchmarkJobStatus.md)

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:104](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L104)
