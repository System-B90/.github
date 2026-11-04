[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiProviderError

# Class: AiProviderError

Defined in: [ui/src/api-server/ai/provider.ts:83](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/ai/provider.ts#L83)

An upstream model backend failed or refused. Distinct from
`ClientApiError`: the caller's request was well-formed, the dependency was
not, so this maps to 502 rather than 400.

## Extends

- `Error`

## Extended by

- [`AiNotConfiguredError`](AiNotConfiguredError.md)

## Constructors

### Constructor

> **new AiProviderError**(`message`, `status?`): `AiProviderError`

Defined in: [ui/src/api-server/ai/provider.ts:87](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/ai/provider.ts#L87)

#### Parameters

##### message

`string`

##### status?

`number`

#### Returns

`AiProviderError`

#### Overrides

`Error.constructor`

## Properties

### status?

> `readonly` `optional` **status?**: `number`

Defined in: [ui/src/api-server/ai/provider.ts:85](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/ai/provider.ts#L85)
