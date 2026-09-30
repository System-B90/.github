[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/gantt/base-item](../index.md) / BuildGantItemRoutesProps

# Type Alias: BuildGantItemRoutesProps\<TEntity, TCreatePayload\>

> **BuildGantItemRoutesProps**\<`TEntity`, `TCreatePayload`\> = `object`

Defined in: [ui/src/app/api/gantt/base-item.ts:9](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/app/api/gantt/base-item.ts#L9)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### TCreatePayload

`TCreatePayload` = `Omit`\<`TEntity`, `"id"`\>

## Properties

### dbSet

> **dbSet**: [`BasicGantOperations`](../../../../../api-shared/types/gantt/api-layer/type-aliases/BasicGantOperations.md)\<`TEntity`, `TCreatePayload`\>

Defined in: [ui/src/app/api/gantt/base-item.ts:13](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/app/api/gantt/base-item.ts#L13)
