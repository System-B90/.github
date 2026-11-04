[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/key-helper](../index.md) / ApiKeyHelper

# Class: ApiKeyHelper

Defined in: [ui/src/api-server/ai/key-helper.ts:31](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/key-helper.ts#L31)

## Implements

- [`AiKeySource`](../../key-source/type-aliases/AiKeySource.md)

## Constructors

### Constructor

> **new ApiKeyHelper**(`options`): `ApiKeyHelper`

Defined in: [ui/src/api-server/ai/key-helper.ts:37](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/key-helper.ts#L37)

#### Parameters

##### options

###### command

`string`

Run through the platform shell (`/bin/sh`, `cmd.exe` on Windows).

###### env

`ProcessEnv`

The helper's environment — where `CC_SSO_BACKEND` reaches it.

#### Returns

`ApiKeyHelper`

## Methods

### get()

> **get**(`signal?`): `Promise`\<`string`\>

Defined in: [ui/src/api-server/ai/key-helper.ts:49](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/key-helper.ts#L49)

#### Parameters

##### signal?

`AbortSignal`

Abandons the wait, not the run: the helper finishes in
the background and its key serves the next request.

#### Returns

`Promise`\<`string`\>

#### Implementation of

`AiKeySource.get`

***

### invalidate()

> **invalidate**(): `void`

Defined in: [ui/src/api-server/ai/key-helper.ts:72](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/key-helper.ts#L72)

#### Returns

`void`

#### Implementation of

`AiKeySource.invalidate`
