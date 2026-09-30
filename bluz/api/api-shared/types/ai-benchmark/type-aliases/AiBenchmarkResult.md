[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-benchmark](../index.md) / AiBenchmarkResult

# Type Alias: AiBenchmarkResult

> **AiBenchmarkResult** = `object`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:77](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L77)

## Properties

### cases

> **cases**: [`AiBenchmarkCase`](AiBenchmarkCase.md)[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:81](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L81)

***

### checksPassed

> **checksPassed**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:86](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L86)

***

### checksTotal

> **checksTotal**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:87](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L87)

***

### durationMs

> **durationMs**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:92](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L92)

***

### gateHeld

> **gateHeld**: `boolean`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:89](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L89)

The approval gate held in every case.

***

### model

> **model**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:78](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L78)

***

### passed

> **passed**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:83](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L83)

Cases whose every check passed.

***

### systemPrompt

> **systemPrompt**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:80](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L80)

The system prompt every case ran under.

***

### total

> **total**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:85](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L85)

Cases run.

***

### totalTokens?

> `optional` **totalTokens?**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:91](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L91)

Total tokens the run spent, so the cost of testing is visible.
