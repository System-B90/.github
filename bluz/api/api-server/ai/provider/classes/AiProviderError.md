[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiProviderError

# Class: AiProviderError

Defined in: [ui/src/api-server/ai/provider.ts:62](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L62)

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

Defined in: [ui/src/api-server/ai/provider.ts:65](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L65)

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

Defined in: [ui/src/api-server/ai/provider.ts:63](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L63)
