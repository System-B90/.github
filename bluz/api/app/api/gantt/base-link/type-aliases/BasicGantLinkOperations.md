[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/gantt/base-link](../index.md) / BasicGantLinkOperations

# Type Alias: BasicGantLinkOperations\<TEntity\>

> **BasicGantLinkOperations**\<`TEntity`\> = `object`

Defined in: [ui/src/app/api/gantt/base-link.ts:9](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/app/api/gantt/base-link.ts#L9)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

## Properties

### linkItem

> **linkItem**: (`newParentId`, `id`) => `Promise`\<[`ApiT`](../../../../../api-shared/types/gantt/api-layer/type-aliases/ApiT.md)\<`TEntity`\>\>

Defined in: [ui/src/app/api/gantt/base-link.ts:10](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/app/api/gantt/base-link.ts#L10)

#### Parameters

##### newParentId

`string`

##### id

`TEntity`\[`"id"`\]

#### Returns

`Promise`\<[`ApiT`](../../../../../api-shared/types/gantt/api-layer/type-aliases/ApiT.md)\<`TEntity`\>\>

***

### unlinkItem

> **unlinkItem**: (`oldParentId`, `id`) => `Promise`\<`void`\>

Defined in: [ui/src/app/api/gantt/base-link.ts:14](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/app/api/gantt/base-link.ts#L14)

#### Parameters

##### oldParentId

`string`

##### id

`TEntity`\[`"id"`\]

#### Returns

`Promise`\<`void`\>
