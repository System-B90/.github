[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-benchmark](../index.md) / AiBenchmarkCase

# Type Alias: AiBenchmarkCase

> **AiBenchmarkCase** = `object`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:24](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai-benchmark.ts#L24)

## Properties

### answer

> **answer**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:34](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai-benchmark.ts#L34)

The model's final prose answer.

***

### checks

> **checks**: [`AiBenchmarkCheck`](AiBenchmarkCheck.md)[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:30](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai-benchmark.ts#L30)

***

### durationMs

> **durationMs**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:36](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai-benchmark.ts#L36)

Wall-clock time for the case.

***

### error?

> `optional` **error?**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:38](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai-benchmark.ts#L38)

Set when the case could not run at all (upstream failure).

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:25](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai-benchmark.ts#L25)

***

### prompt

> **prompt**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:29](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai-benchmark.ts#L29)

The prompt the model was given.

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:27](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai-benchmark.ts#L27)

Hebrew title of what this case probes.

***

### toolCalls

> **toolCalls**: `string`[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:32](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai-benchmark.ts#L32)

Tool names the model called, in order, for the transcript view.
