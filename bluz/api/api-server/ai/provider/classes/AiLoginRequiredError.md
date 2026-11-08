[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiLoginRequiredError

# Class: AiLoginRequiredError

Defined in: [ui/src/api-server/ai/provider.ts:100](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/provider.ts#L100)

The key helper is waiting for an interactive SSO login (cc-sso-helper prints
a `…/login?code=…` link). The browser opens `loginUrl`; the helper keeps
running, and its key serves the next request once the login completes.

## Extends

- [`AiProviderError`](AiProviderError.md)

## Constructors

### Constructor

> **new AiLoginRequiredError**(`loginUrl`): `AiLoginRequiredError`

Defined in: [ui/src/api-server/ai/provider.ts:104](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/provider.ts#L104)

#### Parameters

##### loginUrl

`string`

#### Returns

`AiLoginRequiredError`

#### Overrides

[`AiProviderError`](AiProviderError.md).[`constructor`](AiProviderError.md#constructor)

## Properties

### loginUrl

> `readonly` **loginUrl**: `string`

Defined in: [ui/src/api-server/ai/provider.ts:102](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/provider.ts#L102)

***

### status?

> `readonly` `optional` **status?**: `number`

Defined in: [ui/src/api-server/ai/provider.ts:85](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/provider.ts#L85)

#### Inherited from

[`AiProviderError`](AiProviderError.md).[`status`](AiProviderError.md#status)
