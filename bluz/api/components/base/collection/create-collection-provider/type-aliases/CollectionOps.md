[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/collection/create-collection-provider](../index.md) / CollectionOps

# Type Alias: CollectionOps\<T\>

> **CollectionOps**\<`T`\> = `object`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:76](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/collection/create-collection-provider.tsx#L76)

Optimistic edits a mutation applies to the store before the request runs.

## Type Parameters

### T

`T`

## Properties

### patch

> **patch**: (`key`, `changes`) => `void`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:78](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/collection/create-collection-provider.tsx#L78)

#### Parameters

##### key

`string`

##### changes

`Partial`\<`T`\>

#### Returns

`void`

***

### put

> **put**: (`key`, `item`) => `void`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:77](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/collection/create-collection-provider.tsx#L77)

#### Parameters

##### key

`string`

##### item

`T`

#### Returns

`void`

***

### remove

> **remove**: (`key`) => `void`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:79](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/collection/create-collection-provider.tsx#L79)

#### Parameters

##### key

`string`

#### Returns

`void`
