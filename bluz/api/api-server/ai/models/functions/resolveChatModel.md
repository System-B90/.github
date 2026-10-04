[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/models](../index.md) / resolveChatModel

# Function: resolveChatModel()

> **resolveChatModel**(`provider`, `requested`, `hasOwnKey`): `Promise`\<`string` \| `undefined`\>

Defined in: [ui/src/api-server/ai/models.ts:59](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/models.ts#L59)

The model to send for this user's chat, or undefined for the server default.

## Parameters

### provider

[`AiProvider`](../../provider/type-aliases/AiProvider.md)

The provider the chat will use.

### requested

`string` \| `undefined`

The user's personal model setting ("" = default).

### hasOwnKey

`boolean`

The user chats on their own API key.

## Returns

`Promise`\<`string` \| `undefined`\>
