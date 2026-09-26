[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/tools](../index.md) / AiToolRegistry

# Type Alias: AiToolRegistry

> **AiToolRegistry** = `object`

Defined in: [ui/src/api-server/ai/tools/index.ts:31](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/index.ts#L31)

A set of tools the agent loop may call.

The loop takes one of these rather than reaching for the module-level
registry, so the self-test benchmark can hand it fixture tools that answer
from fabricated data — the same code path, the same approval gate, none of
the user's real records.

## Properties

### find

> **find**: (`name`) => [`AiTool`](../types/type-aliases/AiTool.md)\<`any`\> \| `undefined`

Defined in: [ui/src/api-server/ai/tools/index.ts:32](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/index.ts#L32)

#### Parameters

##### name

`string`

#### Returns

[`AiTool`](../types/type-aliases/AiTool.md)\<`any`\> \| `undefined`

***

### specs

> **specs**: () => [`AiToolSpec`](../../provider/type-aliases/AiToolSpec.md)[]

Defined in: [ui/src/api-server/ai/tools/index.ts:33](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/index.ts#L33)

#### Returns

[`AiToolSpec`](../../provider/type-aliases/AiToolSpec.md)[]

***

### title

> **title**: (`name`) => `string`

Defined in: [ui/src/api-server/ai/tools/index.ts:35](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/index.ts#L35)

Human-facing label for a name, including names not in this registry.

#### Parameters

##### name

`string`

#### Returns

`string`
