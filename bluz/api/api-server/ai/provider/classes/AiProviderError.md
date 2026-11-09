[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiProviderError

# Class: AiProviderError

Defined in: [ui/src/api-server/ai/provider.ts:83](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/ai/provider.ts#L83)

An upstream model backend failed or refused. Distinct from
`ClientApiError`: the caller's request was well-formed, the dependency was
not, so this maps to 502 rather than 400.

## Extends

- `Error`

## Extended by

- [`AiLoginRequiredError`](AiLoginRequiredError.md)
- [`AiNotConfiguredError`](AiNotConfiguredError.md)

## Constructors

### Constructor

> **new AiProviderError**(`message`, `status?`): `AiProviderError`

Defined in: [ui/src/api-server/ai/provider.ts:87](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/ai/provider.ts#L87)

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

Defined in: [ui/src/api-server/ai/provider.ts:85](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/ai/provider.ts#L85)
