[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/tools](../index.md) / AiToolRegistry

# Type Alias: AiToolRegistry

> **AiToolRegistry** = `object`

Defined in: [ui/src/api-server/ai/tools/index.ts:37](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/index.ts#L37)

A set of tools the agent loop may call.

The loop takes one of these rather than reaching for the module-level
registry, so the self-test benchmark can hand it fixture tools that answer
from fabricated data — the same code path, the same approval gate, none of
the user's real records.

## Properties

### find

> **find**: (`name`) => [`AiTool`](../types/type-aliases/AiTool.md)\<`any`\> \| `undefined`

Defined in: [ui/src/api-server/ai/tools/index.ts:38](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/index.ts#L38)

#### Parameters

##### name

`string`

#### Returns

[`AiTool`](../types/type-aliases/AiTool.md)\<`any`\> \| `undefined`

***

### specs

> **specs**: () => [`AiToolSpec`](../../provider/type-aliases/AiToolSpec.md)[]

Defined in: [ui/src/api-server/ai/tools/index.ts:39](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/index.ts#L39)

#### Returns

[`AiToolSpec`](../../provider/type-aliases/AiToolSpec.md)[]

***

### title

> **title**: (`name`) => `string`

Defined in: [ui/src/api-server/ai/tools/index.ts:41](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/index.ts#L41)

Human-facing label for a name, including names not in this registry.

#### Parameters

##### name

`string`

#### Returns

`string`
