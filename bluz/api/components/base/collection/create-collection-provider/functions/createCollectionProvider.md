[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/collection/create-collection-provider](../index.md) / createCollectionProvider

# Function: createCollectionProvider()

> **createCollectionProvider**\<`T`, `TId`, `TCreate`\>(`config`): `object`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:145](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/base/collection/create-collection-provider.tsx#L145)

Builds an optimistic-CRUD-with-rollback provider around a REST collection:
loads on mount, applies edits locally, rolls the whole map back when the
request fails, and keeps itself fresh from a websocket update message.

## Type Parameters

### T

`T`

### TId

`TId`

### TCreate

`TCreate`

## Parameters

### config

[`CollectionConfig`](../type-aliases/CollectionConfig.md)\<`T`, `TId`, `TCreate`\>

## Returns

`object`

### Provider

> **Provider**: (`__namedParameters`) => `Element`

#### Parameters

##### \_\_namedParameters

###### children

`ReactNode`

#### Returns

`Element`

### useCollection

> **useCollection**: (`hookName`) => [`CollectionContextState`](../type-aliases/CollectionContextState.md)\<`T`, `TCreate`\>

#### Parameters

##### hookName

`string`

#### Returns

[`CollectionContextState`](../type-aliases/CollectionContextState.md)\<`T`, `TCreate`\>
