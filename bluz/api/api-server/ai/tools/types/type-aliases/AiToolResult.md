[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/types](../index.md) / AiToolResult

# Type Alias: AiToolResult

> **AiToolResult** = `object`

Defined in: [ui/src/api-server/ai/tools/types.ts:51](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/types.ts#L51)

## Properties

### data

> **data**: `unknown`

Defined in: [ui/src/api-server/ai/tools/types.ts:53](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/types.ts#L53)

Returned to the model. Keep it compact — it is re-sent every turn.

***

### hints?

> `optional` **hints?**: `string`[]

Defined in: [ui/src/api-server/ai/tools/types.ts:61](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/types.ts#L61)

Guidance that depends on what this call returned, e.g. a rule that only
matters when the payload holds people. Keeps the system prompt short:
the model learns a rule at the moment it needs it.

***

### summary

> **summary**: `string`

Defined in: [ui/src/api-server/ai/tools/types.ts:55](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/types.ts#L55)

One Hebrew line shown in the chat transcript.
