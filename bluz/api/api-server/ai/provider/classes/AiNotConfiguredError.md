[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiNotConfiguredError

# Class: AiNotConfiguredError

Defined in: [ui/src/api-server/ai/provider.ts:95](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/provider.ts#L95)

Raised when the deployment has no usable AI configuration.

## Extends

- [`AiProviderError`](AiProviderError.md)

## Constructors

### Constructor

> **new AiNotConfiguredError**(`message`): `AiNotConfiguredError`

Defined in: [ui/src/api-server/ai/provider.ts:96](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/provider.ts#L96)

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

Defined in: [ui/src/api-server/ai/provider.ts:85](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/provider.ts#L85)

#### Inherited from

[`AiProviderError`](AiProviderError.md).[`status`](AiProviderError.md#status)
