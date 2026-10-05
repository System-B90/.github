[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AiToolCall

# Type Alias: AiToolCall

> **AiToolCall** = `object`

Defined in: [ui/src/api-shared/types/ai.ts:28](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/ai.ts#L28)

A tool invocation requested by the model. `arguments` stays a raw JSON
string, exactly as the model emitted it: it is not always valid JSON, and
the transcript replayed on the next turn must be byte-identical to what the
backend produced.

## Properties

### arguments

> **arguments**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:31](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/ai.ts#L31)

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:29](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/ai.ts#L29)

***

### name

> **name**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:30](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/ai.ts#L30)
