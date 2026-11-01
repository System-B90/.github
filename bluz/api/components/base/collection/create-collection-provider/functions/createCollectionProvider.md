[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/collection/create-collection-provider](../index.md) / createCollectionProvider

# Function: createCollectionProvider()

> **createCollectionProvider**\<`T`, `TId`, `TCreate`\>(`config`): `object`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:151](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/base/collection/create-collection-provider.tsx#L151)

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
