[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/cases](../index.md) / AiBenchmarkObservation

# Type Alias: AiBenchmarkObservation

> **AiBenchmarkObservation** = `object`

Defined in: [ui/src/api-server/ai/benchmark/cases.ts:34](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/benchmark/cases.ts#L34)

What one case observed about a run, for its checks to grade.

## Properties

### answer

> **answer**: `string`

Defined in: [ui/src/api-server/ai/benchmark/cases.ts:43](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/benchmark/cases.ts#L43)

***

### askedUser

> **askedUser**: `boolean`

Defined in: [ui/src/api-server/ai/benchmark/cases.ts:42](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/benchmark/cases.ts#L42)

Whether the model asked the human a question.

***

### executedWrites

> **executedWrites**: `string`[]

Defined in: [ui/src/api-server/ai/benchmark/cases.ts:40](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/benchmark/cases.ts#L40)

Write tools that actually executed. Must always be empty.

***

### proposals

> **proposals**: `ObservedCall`[]

Defined in: [ui/src/api-server/ai/benchmark/cases.ts:47](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/benchmark/cases.ts#L47)

Every write proposed for approval, with its arguments.

***

### proposedWrites

> **proposedWrites**: `string`[]

Defined in: [ui/src/api-server/ai/benchmark/cases.ts:38](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/benchmark/cases.ts#L38)

Write tools the model proposed (and which the gate stopped).

***

### reads

> **reads**: `ObservedCall`[]

Defined in: [ui/src/api-server/ai/benchmark/cases.ts:45](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/benchmark/cases.ts#L45)

Every read that ran, with its arguments.

***

### toolCalls

> **toolCalls**: `string`[]

Defined in: [ui/src/api-server/ai/benchmark/cases.ts:36](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/benchmark/cases.ts#L36)

Tool names called, in order. Includes calls that only got proposed.
