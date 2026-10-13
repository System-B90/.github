[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-benchmark](../index.md) / AiBenchmarkResult

# Type Alias: AiBenchmarkResult

> **AiBenchmarkResult** = `object`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:84](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-benchmark.ts#L84)

## Properties

### cases

> **cases**: [`AiBenchmarkCase`](AiBenchmarkCase.md)[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:91](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-benchmark.ts#L91)

***

### checksPassed

> **checksPassed**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:96](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-benchmark.ts#L96)

***

### checksTotal

> **checksTotal**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:97](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-benchmark.ts#L97)

***

### durationMs

> **durationMs**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:107](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-benchmark.ts#L107)

***

### gateHeld

> **gateHeld**: `boolean`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:99](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-benchmark.ts#L99)

The approval gate held in every case.

***

### model

> **model**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:85](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-benchmark.ts#L85)

***

### modelWarning?

> `optional` **modelWarning?**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:104](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-benchmark.ts#L104)

Set when the backend lists its models and `AI_MODEL` is not among them
(#779): the typo that otherwise only shows up as a 404 at chat time.

***

### passed

> **passed**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:93](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-benchmark.ts#L93)

Cases whose every check passed.

***

### seed?

> `optional` **seed?**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:88](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-benchmark.ts#L88)

***

### systemPrompt

> **systemPrompt**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:90](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-benchmark.ts#L90)

The system prompt every case ran under.

***

### temperature?

> `optional` **temperature?**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:87](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-benchmark.ts#L87)

Sampling every case ran with, so two reports can be compared (#948).

***

### total

> **total**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:95](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-benchmark.ts#L95)

Cases run.

***

### totalTokens?

> `optional` **totalTokens?**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:106](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-benchmark.ts#L106)

Total tokens the run spent, so the cost of testing is visible.
