[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiNotConfiguredError

# Class: AiNotConfiguredError

Defined in: [ui/src/api-server/ai/provider.ts:73](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L73)

Raised when the deployment has no usable AI configuration.

## Extends

- [`AiProviderError`](AiProviderError.md)

## Constructors

### Constructor

> **new AiNotConfiguredError**(`message`): `AiNotConfiguredError`

Defined in: [ui/src/api-server/ai/provider.ts:74](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L74)

#### Parameters

##### message

`string`

#### Returns

`AiNotConfiguredError`

#### Overrides

[`AiProviderError`](AiProviderError.md).[`constructor`](AiProviderError.md#constructor)

## Properties

### status?

> `readonly` `optional` **status?**: `number`

Defined in: [ui/src/api-server/ai/provider.ts:63](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L63)

#### Inherited from

[`AiProviderError`](AiProviderError.md).[`status`](AiProviderError.md#status)
