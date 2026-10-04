[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiNotConfiguredError

# Class: AiNotConfiguredError

Defined in: [ui/src/api-server/ai/provider.ts:95](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/provider.ts#L95)

Raised when the deployment has no usable AI configuration.

## Extends

- [`AiProviderError`](AiProviderError.md)

## Constructors

### Constructor

> **new AiNotConfiguredError**(`message`): `AiNotConfiguredError`

Defined in: [ui/src/api-server/ai/provider.ts:96](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/provider.ts#L96)

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

Defined in: [ui/src/api-server/ai/provider.ts:85](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/provider.ts#L85)

#### Inherited from

[`AiProviderError`](AiProviderError.md).[`status`](AiProviderError.md#status)
