[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/collection/create-collection-provider](../index.md) / CollectionConfig

# Type Alias: CollectionConfig\<T, TId, TCreate\>

> **CollectionConfig**\<`T`, `TId`, `TCreate`\> = `object`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:96](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/collection/create-collection-provider.tsx#L96)

## Type Parameters

### T

`T`

### TId

`TId`

### TCreate

`TCreate`

## Properties

### api

> **api**: [`CollectionApi`](CollectionApi.md)\<`T`, `TId`\>

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:97](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/collection/create-collection-provider.tsx#L97)

***

### buildItem

> **buildItem**: (`data`) => `T`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:104](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/collection/create-collection-provider.tsx#L104)

Builds the optimistic item — including its temporary id — from form data.

#### Parameters

##### data

`TCreate`

#### Returns

`T`

***

### getId

> **getId**: (`item`) => `TId`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:100](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/collection/create-collection-provider.tsx#L100)

#### Parameters

##### item

`T`

#### Returns

`TId`

***

### getKey

> **getKey**: (`item`) => `string`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:99](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/collection/create-collection-provider.tsx#L99)

Stable store key. May be composite (e.g. rooms key on `source:id`).

#### Parameters

##### item

`T`

#### Returns

`string`

***

### getLabel

> **getLabel**: (`item`) => `string`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:102](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/collection/create-collection-provider.tsx#L102)

Human-readable name used in the Hebrew snackbar texts.

#### Parameters

##### item

`T`

#### Returns

`string`

***

### messages

> **messages**: `object`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:105](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/collection/create-collection-provider.tsx#L105)

#### createFailure

> **createFailure**: (`label`) => `string`

##### Parameters

###### label

`string`

##### Returns

`string`

#### createSuccess

> **createSuccess**: (`label`) => `string`

##### Parameters

###### label

`string`

##### Returns

`string`

#### deleteFailure

> **deleteFailure**: (`label`) => `string`

##### Parameters

###### label

`string`

##### Returns

`string`

#### deleteSuccess

> **deleteSuccess**: (`label`) => `string`

##### Parameters

###### label

`string`

##### Returns

`string`

#### loadFailed

> **loadFailed**: `string`

#### updateFailure

> **updateFailure**: (`label`) => `string`

##### Parameters

###### label

`string`

##### Returns

`string`

#### updateSuccess

> **updateSuccess**: (`label`) => `string`

##### Parameters

###### label

`string`

##### Returns

`string`

***

### websocket

> **websocket**: `object`

Defined in: [ui/src/components/base/collection/create-collection-provider.tsx:114](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/collection/create-collection-provider.tsx#L114)

#### keyOf?

> `optional` **keyOf?**: (`id`, `item`) => `string`

Maps an id from the incremental WS map to a store key. Defaults to the id.

##### Parameters

###### id

`string`

###### item

`null` \| `T`

##### Returns

`string`

#### messageType

> **messageType**: [`MessageTypes`](../../../../../settings/enumerations/MessageTypes.md)

#### payloadKey?

> `optional` **payloadKey?**: `string`

Field on the WS payload holding an incremental `id -> item | null` map.
Omit it — or send a payload without the field — to force a full reload.
