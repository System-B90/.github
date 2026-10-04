[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-benchmark](../index.md) / AiBenchmarkResult

# Type Alias: AiBenchmarkResult

> **AiBenchmarkResult** = `object`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:77](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L77)

## Properties

### cases

> **cases**: [`AiBenchmarkCase`](AiBenchmarkCase.md)[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:81](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L81)

***

### checksPassed

> **checksPassed**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:86](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L86)

***

### checksTotal

> **checksTotal**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:87](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L87)

***

### durationMs

> **durationMs**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:97](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L97)

***

### gateHeld

> **gateHeld**: `boolean`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:89](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L89)

The approval gate held in every case.

***

### model

> **model**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:78](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L78)

***

### modelWarning?

> `optional` **modelWarning?**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:94](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L94)

Set when the backend lists its models and `AI_MODEL` is not among them
(#779): the typo that otherwise only shows up as a 404 at chat time.

***

### passed

> **passed**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:83](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L83)

Cases whose every check passed.

***

### systemPrompt

> **systemPrompt**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:80](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L80)

The system prompt every case ran under.

***

### total

> **total**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:85](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L85)

Cases run.

***

### totalTokens?

> `optional` **totalTokens?**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:96](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L96)

Total tokens the run spent, so the cost of testing is visible.
