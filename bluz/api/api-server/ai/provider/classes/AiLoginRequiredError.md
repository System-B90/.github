[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiLoginRequiredError

# Class: AiLoginRequiredError

Defined in: [ui/src/api-server/ai/provider.ts:100](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/ai/provider.ts#L100)

The key helper is waiting for an interactive SSO login (cc-sso-helper prints
a `…/login?code=…` link). The browser opens `loginUrl`; the helper keeps
running, and its key serves the next request once the login completes.

## Extends

- [`AiProviderError`](AiProviderError.md)

## Constructors

### Constructor

> **new AiLoginRequiredError**(`loginUrl`): `AiLoginRequiredError`

Defined in: [ui/src/api-server/ai/provider.ts:104](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/ai/provider.ts#L104)

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

Defined in: [ui/src/api-server/ai/provider.ts:102](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/ai/provider.ts#L102)

***

### status?

> `readonly` `optional` **status?**: `number`

Defined in: [ui/src/api-server/ai/provider.ts:85](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/ai/provider.ts#L85)

#### Inherited from

[`AiProviderError`](AiProviderError.md).[`status`](AiProviderError.md#status)
