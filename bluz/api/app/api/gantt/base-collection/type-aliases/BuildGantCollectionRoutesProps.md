[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/gantt/base-collection](../index.md) / BuildGantCollectionRoutesProps

# Type Alias: BuildGantCollectionRoutesProps\<TEntity, TCreatePayload\>

> **BuildGantCollectionRoutesProps**\<`TEntity`, `TCreatePayload`\> = `object`

Defined in: [ui/src/app/api/gantt/base-collection.ts:22](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/app/api/gantt/base-collection.ts#L22)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### TCreatePayload

`TCreatePayload` = `Omit`\<`TEntity`, `"id"`\>

## Properties

### dbSet

> **dbSet**: [`BasicGantOperations`](../../../../../api-shared/types/gantt/api-layer/type-aliases/BasicGantOperations.md)\<`TEntity`, `TCreatePayload`\>

Defined in: [ui/src/app/api/gantt/base-collection.ts:26](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/app/api/gantt/base-collection.ts#L26)
