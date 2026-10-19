[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-benchmark](../index.md) / AiBenchmarkCase

# Type Alias: AiBenchmarkCase

> **AiBenchmarkCase** = `object`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:26](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L26)

## Properties

### answer

> **answer**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:36](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L36)

The model's final prose answer.

***

### checks

> **checks**: [`AiBenchmarkCheck`](AiBenchmarkCheck.md)[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:32](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L32)

***

### durationMs

> **durationMs**: `number`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:47](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L47)

Wall-clock time for the case.

***

### error?

> `optional` **error?**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:56](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L56)

Set when the case could not run at all (upstream failure).

***

### gateHeld

> **gateHeld**: `boolean`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:63](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L63)

No write ran without approval. Structural, not a model skill, so it is
reported beside the score rather than padding it.

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:27](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L27)

***

### model?

> `optional` **model?**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:52](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L52)

The model that actually answered, as the provider named it. Differs
from the run's `model` when that is a router (#948).

***

### passed

> **passed**: `boolean`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:58](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L58)

Every check passed: the unit the headline score counts.

***

### prompt

> **prompt**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:31](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L31)

The prompt the model was given.

***

### proposals

> **proposals**: `object`[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:43](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L43)

Write proposals the gate stopped, with their parsed arguments.

#### args

> **args**: `Record`\<`string`, `unknown`\>

#### name

> **name**: `string`

***

### reasoning?

> `optional` **reasoning?**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:45](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L45)

Reasoning/chain-of-thought text, when the model streamed any.

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:29](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L29)

Hebrew title of what this case probes.

***

### tokens?

> `optional` **tokens?**: `object`

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:54](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L54)

Tokens the case spent, split so prompt bloat is visible (#948).

#### completion

> **completion**: `number`

#### prompt

> **prompt**: `number`

#### total

> **total**: `number`

***

### toolCalls

> **toolCalls**: `string`[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:34](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L34)

Tool names the model called, in order, for the transcript view.

***

### transcript

> **transcript**: [`AiMessage`](../../ai/type-aliases/AiMessage.md)[]

Defined in: [ui/src/api-shared/types/ai-benchmark.ts:41](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/ai-benchmark.ts#L41)

Every message the agent loop produced — assistant turns, tool calls and
the raw tool results — for the JSON export used to debug tools/prompts.
