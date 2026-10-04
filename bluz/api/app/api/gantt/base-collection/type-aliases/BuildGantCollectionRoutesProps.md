[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/gantt/base-collection](../index.md) / BuildGantCollectionRoutesProps

# Type Alias: BuildGantCollectionRoutesProps\<TEntity, TCreatePayload\>

> **BuildGantCollectionRoutesProps**\<`TEntity`, `TCreatePayload`\> = `object`

Defined in: [ui/src/app/api/gantt/base-collection.ts:21](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/app/api/gantt/base-collection.ts#L21)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### TCreatePayload

`TCreatePayload` = `Omit`\<`TEntity`, `"id"`\>

## Properties

### dbSet

> **dbSet**: [`BasicGantOperations`](../../../../../api-shared/types/gantt/api-layer/type-aliases/BasicGantOperations.md)\<`TEntity`, `TCreatePayload`\>

Defined in: [ui/src/app/api/gantt/base-collection.ts:25](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/app/api/gantt/base-collection.ts#L25)
