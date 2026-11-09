[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/collection/create-collection-provider](../index.md) / CollectionContextState

# Type Alias: CollectionContextState\<T, TCreate\>

> **CollectionContextState**\<`T`, `TCreate`\> = `object`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:128](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/collection/create-collection-provider.tsx#L128)

## Type Parameters

### T

`T`

### TCreate

`TCreate`

## Properties

### addItem

> **addItem**: (`data`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:137](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/collection/create-collection-provider.tsx#L137)

Mutations report failure with a snackbar and resolve to `false`
instead of rejecting, so a form can keep what was typed.

#### Parameters

##### data

`TCreate`

#### Returns

`Promise`\<`boolean`\>

***

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:129](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/collection/create-collection-provider.tsx#L129)

***

### deleteItem

> **deleteItem**: (`key`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:141](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/collection/create-collection-provider.tsx#L141)

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`boolean`\>

***

### getItem

> **getItem**: (`key`) => `T` \| `undefined`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:132](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/collection/create-collection-provider.tsx#L132)

#### Parameters

##### key

`string`

#### Returns

`T` \| `undefined`

***

### isLoading

> **isLoading**: `boolean`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:131](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/collection/create-collection-provider.tsx#L131)

***

### items

> **items**: `T`[]

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:130](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/collection/create-collection-provider.tsx#L130)

***

### mutate

> **mutate**: (`mutation`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:143](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/collection/create-collection-provider.tsx#L143)

Escape hatch for collection-specific writes (e.g. room extended info).

#### Parameters

##### mutation

[`CollectionMutation`](CollectionMutation.md)\<`T`\>

#### Returns

`Promise`\<`boolean`\>

***

### patchItem

> **patchItem**: (`key`, `changes`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:140](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/collection/create-collection-provider.tsx#L140)

Merges `changes` into the stored item and persists the merged result.

#### Parameters

##### key

`string`

##### changes

`Partial`\<`T`\>

#### Returns

`Promise`\<`boolean`\>

***

### updateItem

> **updateItem**: (`item`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:138](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/collection/create-collection-provider.tsx#L138)

#### Parameters

##### item

`T`

#### Returns

`Promise`\<`boolean`\>
