[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/user-ai](../index.md) / UserAi

# Type Alias: UserAi

> **UserAi** = `object`

Defined in: [ui/src/api-server/ai/user-ai.ts:11](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/user-ai.ts#L11)

## Properties

### chatModel

> **chatModel**: (`provider`) => `Promise`\<`string` \| `undefined`\>

Defined in: [ui/src/api-server/ai/user-ai.ts:22](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/user-ai.ts#L22)

The model to send, or undefined for the provider's default.

#### Parameters

##### provider

[`AiProvider`](../../provider/type-aliases/AiProvider.md)

#### Returns

`Promise`\<`string` \| `undefined`\>

***

### configured

> **configured**: `boolean`

Defined in: [ui/src/api-server/ai/user-ai.ts:15](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/user-ai.ts#L15)

AI is usable for this user: the server's key or their own.

***

### provider

> **provider**: () => [`AiProvider`](../../provider/type-aliases/AiProvider.md)

Defined in: [ui/src/api-server/ai/user-ai.ts:20](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/user-ai.ts#L20)

The provider chat would use.

#### Returns

[`AiProvider`](../../provider/type-aliases/AiProvider.md)

#### Throws

AiNotConfiguredError when neither key is set.

***

### userKey

> **userKey**: `string` \| `undefined`

Defined in: [ui/src/api-server/ai/user-ai.ts:13](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/user-ai.ts#L13)

The user's own API key, when set.
