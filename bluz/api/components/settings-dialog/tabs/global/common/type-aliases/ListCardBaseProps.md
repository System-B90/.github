[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/settings-dialog/tabs/global/common](../index.md) / ListCardBaseProps

# Type Alias: ListCardBaseProps\<TEntity\>

> **ListCardBaseProps**\<`TEntity`\> = `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:7](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L7)

## Type Parameters

### TEntity

`TEntity`

## Properties

### filteredEntities

> **filteredEntities**: `TEntity`[]

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:8](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L8)

***

### handleDelete

> **handleDelete**: (`id`) => `Promise`\<`void`\>

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:16](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L16)

#### Parameters

##### id

`string`

#### Returns

`Promise`\<`void`\>

***

### handleStartCreate

> **handleStartCreate**: () => `void`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:15](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L15)

#### Returns

`void`

***

### isLoading?

> `optional` **isLoading?**: `boolean`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:10](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L10)

Renders skeleton rows instead of "no entries" while the fetch is in flight.

***

### populateFormFrom

> **populateFormFrom**: (`entity`) => `void`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:14](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L14)

#### Parameters

##### entity

`TEntity`

#### Returns

`void`

***

### searchQuery

> **searchQuery**: `string`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:11](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L11)

***

### selectedEntity

> **selectedEntity**: `null` \| `TEntity`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:13](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L13)

***

### setSearchQuery

> **setSearchQuery**: (`query`) => `void`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:12](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L12)

#### Parameters

##### query

`string`

#### Returns

`void`
