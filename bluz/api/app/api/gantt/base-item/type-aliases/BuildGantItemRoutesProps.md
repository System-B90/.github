[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/gantt/base-item](../index.md) / BuildGantItemRoutesProps

# Type Alias: BuildGantItemRoutesProps\<TEntity, TCreatePayload\>

> **BuildGantItemRoutesProps**\<`TEntity`, `TCreatePayload`\> = `object`

Defined in: [ui/src/app/api/gantt/base-item.ts:9](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/app/api/gantt/base-item.ts#L9)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### TCreatePayload

`TCreatePayload` = `Omit`\<`TEntity`, `"id"`\>

## Properties

### dbSet

> **dbSet**: [`BasicGantOperations`](../../../../../api-shared/types/gantt/api-layer/type-aliases/BasicGantOperations.md)\<`TEntity`, `TCreatePayload`\>

Defined in: [ui/src/app/api/gantt/base-item.ts:13](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/app/api/gantt/base-item.ts#L13)
