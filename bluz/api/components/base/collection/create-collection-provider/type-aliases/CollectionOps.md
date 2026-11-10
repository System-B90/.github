[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/collection/create-collection-provider](../index.md) / CollectionOps

# Type Alias: CollectionOps\<T\>

> **CollectionOps**\<`T`\> = `object`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:78](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/base/collection/create-collection-provider.tsx#L78)

Optimistic edits a mutation applies to the store before the request runs.

## Type Parameters

### T

`T`

## Properties

### patch

> **patch**: (`key`, `changes`) => `void`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:80](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/base/collection/create-collection-provider.tsx#L80)

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

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:79](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/base/collection/create-collection-provider.tsx#L79)

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

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:81](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/base/collection/create-collection-provider.tsx#L81)

#### Parameters

##### key

`string`

#### Returns

`void`
