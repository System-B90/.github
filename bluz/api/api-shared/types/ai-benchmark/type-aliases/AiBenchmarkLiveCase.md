[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-benchmark](../index.md) / AiBenchmarkLiveCase

# Type Alias: AiBenchmarkLiveCase

> **AiBenchmarkLiveCase** = `object`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:73](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/ai-benchmark.ts#L73)

One case as the run progresses, for the live view.

## Properties

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:74](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/ai-benchmark.ts#L74)

***

### prompt

> **prompt**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:76](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/ai-benchmark.ts#L76)

***

### result?

> `optional` **result?**: [`AiBenchmarkCase`](AiBenchmarkCase.md)

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:81](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/ai-benchmark.ts#L81)

Set once the case is done.

***

### state

> **state**: [`AiBenchmarkCaseState`](../enumerations/AiBenchmarkCaseState.md)

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:77](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/ai-benchmark.ts#L77)

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:75](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/ai-benchmark.ts#L75)

***

### toolCalls

> **toolCalls**: `string`[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:79](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/ai-benchmark.ts#L79)

Tools called so far; grows while the case runs.
