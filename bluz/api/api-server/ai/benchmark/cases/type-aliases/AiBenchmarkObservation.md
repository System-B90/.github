[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/cases](../index.md) / AiBenchmarkObservation

# Type Alias: AiBenchmarkObservation

> **AiBenchmarkObservation** = `object`

Defined in: [ui/src/api-server/ai/benchmark/cases.ts:18](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/benchmark/cases.ts#L18)

What one case observed about a run, for its checks to grade.

## Properties

### answer

> **answer**: `string`

Defined in: [ui/src/api-server/ai/benchmark/cases.ts:27](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/benchmark/cases.ts#L27)

***

### askedUser

> **askedUser**: `boolean`

Defined in: [ui/src/api-server/ai/benchmark/cases.ts:26](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/benchmark/cases.ts#L26)

Whether the model asked the human a question.

***

### executedWrites

> **executedWrites**: `string`[]

Defined in: [ui/src/api-server/ai/benchmark/cases.ts:24](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/benchmark/cases.ts#L24)

Write tools that actually executed. Must always be empty.

***

### proposedWrites

> **proposedWrites**: `string`[]

Defined in: [ui/src/api-server/ai/benchmark/cases.ts:22](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/benchmark/cases.ts#L22)

Write tools the model proposed (and which the gate stopped).

***

### toolCalls

> **toolCalls**: `string`[]

Defined in: [ui/src/api-server/ai/benchmark/cases.ts:20](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/benchmark/cases.ts#L20)

Tool names called, in order. Includes calls that only got proposed.
