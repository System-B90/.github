[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/key-helper](../index.md) / ApiKeyHelper

# Class: ApiKeyHelper

Defined in: [ui/src/api-server/ai/key-helper.ts:86](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/ai/key-helper.ts#L86)

## Implements

- [`AiKeySource`](../../key-source/type-aliases/AiKeySource.md)

## Constructors

### Constructor

> **new ApiKeyHelper**(`options`): `ApiKeyHelper`

Defined in: [ui/src/api-server/ai/key-helper.ts:95](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/ai/key-helper.ts#L95)

#### Parameters

##### options

###### command

`string`

Run through the platform shell (`/bin/sh`, `cmd.exe` on Windows).

###### env

`ProcessEnv`

The helper's environment — where `CC_SSO_BACKEND` reaches it.

###### keyFile?

`string`

File the helper writes its key to; read after each successful run.

#### Returns

`ApiKeyHelper`

## Methods

### get()

> **get**(`signal?`): `Promise`\<`string`\>

Defined in: [ui/src/api-server/ai/key-helper.ts:110](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/ai/key-helper.ts#L110)

#### Parameters

##### signal?

`AbortSignal`

Abandons the wait, not the run: the helper finishes in
the background and its key serves the next request.

#### Returns

`Promise`\<`string`\>

#### Throws

AiLoginRequiredError when the helper waits on an SSO login.

#### Implementation of

`AiKeySource.get`

***

### invalidate()

> **invalidate**(): `void`

Defined in: [ui/src/api-server/ai/key-helper.ts:139](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/ai/key-helper.ts#L139)

#### Returns

`void`

#### Implementation of

`AiKeySource.invalidate`
