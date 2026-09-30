[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-benchmark](../index.md) / AiBenchmarkLiveCase

# Type Alias: AiBenchmarkLiveCase

> **AiBenchmarkLiveCase** = `object`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:66](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L66)

One case as the run progresses, for the live view.

## Properties

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:67](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L67)

***

### prompt

> **prompt**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:69](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L69)

***

### result?

> `optional` **result?**: [`AiBenchmarkCase`](AiBenchmarkCase.md)

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:74](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L74)

Set once the case is done.

***

### state

> **state**: [`AiBenchmarkCaseState`](../enumerations/AiBenchmarkCaseState.md)

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:70](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L70)

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:68](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L68)

***

### toolCalls

> **toolCalls**: `string`[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:72](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/ai-benchmark.ts#L72)

Tools called so far; grows while the case runs.
