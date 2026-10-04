[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-benchmark](../index.md) / AiBenchmarkCase

# Type Alias: AiBenchmarkCase

> **AiBenchmarkCase** = `object`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:26](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L26)

## Properties

### answer

> **answer**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:36](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L36)

The model's final prose answer.

***

### checks

> **checks**: [`AiBenchmarkCheck`](AiBenchmarkCheck.md)[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:32](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L32)

***

### durationMs

> **durationMs**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:47](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L47)

Wall-clock time for the case.

***

### error?

> `optional` **error?**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:49](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L49)

Set when the case could not run at all (upstream failure).

***

### gateHeld

> **gateHeld**: `boolean`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:56](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L56)

No write ran without approval. Structural, not a model skill, so it is
reported beside the score rather than padding it.

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:27](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L27)

***

### passed

> **passed**: `boolean`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:51](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L51)

Every check passed: the unit the headline score counts.

***

### prompt

> **prompt**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:31](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L31)

The prompt the model was given.

***

### proposals

> **proposals**: `object`[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:43](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L43)

Write proposals the gate stopped, with their parsed arguments.

#### args

> **args**: `Record`\<`string`, `unknown`\>

#### name

> **name**: `string`

***

### reasoning?

> `optional` **reasoning?**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:45](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L45)

Reasoning/chain-of-thought text, when the model streamed any.

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:29](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L29)

Hebrew title of what this case probes.

***

### toolCalls

> **toolCalls**: `string`[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:34](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L34)

Tool names the model called, in order, for the transcript view.

***

### transcript

> **transcript**: [`AiMessage`](../../ai/type-aliases/AiMessage.md)[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:41](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-benchmark.ts#L41)

Every message the agent loop produced — assistant turns, tool calls and
the raw tool results — for the JSON export used to debug tools/prompts.
