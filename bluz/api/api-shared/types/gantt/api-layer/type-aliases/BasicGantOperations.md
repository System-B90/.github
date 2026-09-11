[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/api-layer](../index.md) / BasicGantOperations

# Type Alias: BasicGantOperations\<TEntity, TCreatePayload\>

> **BasicGantOperations**\<`TEntity`, `TCreatePayload`\> = `object`

Defined in: [ui/src/api-shared/types/gantt/api-layer.ts:37](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/api-layer.ts#L37)

The DB-facing operations a Gantt entity must provide for the generic
collection/item route builders. Declared here so `api-server` can implement
it without importing from the route layer that consumes it.

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../models/shared/type-aliases/BaseGantItem.md)

### TCreatePayload

`TCreatePayload` = `Omit`\<`TEntity`, `"id"`\>

## Properties

### createNewItem

> **createNewItem**: (`payload`) => `Promise`\<[`ApiT`](ApiT.md)\<`TEntity`\> \| `TEntity`\>

Defined in: [ui/src/api-shared/types/gantt/api-layer.ts:49](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/api-layer.ts#L49)

#### Parameters

##### payload

`TCreatePayload`

#### Returns

`Promise`\<[`ApiT`](ApiT.md)\<`TEntity`\> \| `TEntity`\>

***

### deleteItem

> **deleteItem**: (`id`) => `Promise`\<`void`\>

Defined in: [ui/src/api-shared/types/gantt/api-layer.ts:56](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/api-layer.ts#L56)

#### Parameters

##### id

`TEntity`\[`"id"`\]

#### Returns

`Promise`\<`void`\>

***

### getItem

> **getItem**: (`id`) => `Promise`\<`any`\>

Defined in: [ui/src/api-shared/types/gantt/api-layer.ts:48](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/api-layer.ts#L48)

#### Parameters

##### id

`TEntity`\[`"id"`\]

#### Returns

`Promise`\<`any`\>

***

### getMultipleItems

> **getMultipleItems**: (`ids`) => `Promise`\<`TEntity`[]\>

Defined in: [ui/src/api-shared/types/gantt/api-layer.ts:47](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/api-layer.ts#L47)

#### Parameters

##### ids

`string`[]

#### Returns

`Promise`\<`TEntity`[]\>

***

### listItems

> **listItems**: (`withParents?`) => `Promise`\<`Record`\<`TEntity`\[`"id"`\], \{ `title`: `TEntity`\[`"title"`\]; \}\> \| `Record`\<`TEntity`\[`"id"`\], `TEntity`\[`"title"`\]\>\>

Defined in: [ui/src/api-shared/types/gantt/api-layer.ts:41](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/api-layer.ts#L41)

#### Parameters

##### withParents?

`boolean`

#### Returns

`Promise`\<`Record`\<`TEntity`\[`"id"`\], \{ `title`: `TEntity`\[`"title"`\]; \}\> \| `Record`\<`TEntity`\[`"id"`\], `TEntity`\[`"title"`\]\>\>

***

### updateItem

> **updateItem**: (`id`, `updates`) => `Promise`\<`TEntity`\>

Defined in: [ui/src/api-shared/types/gantt/api-layer.ts:52](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/api-layer.ts#L52)

#### Parameters

##### id

`TEntity`\[`"id"`\]

##### updates

`Partial`\<`TEntity`\>

#### Returns

`Promise`\<`TEntity`\>
