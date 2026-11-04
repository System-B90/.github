[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/base](../index.md) / clientGantApiBuilder

# Function: clientGantApiBuilder()

> **clientGantApiBuilder**\<`TEntity`, `TCreatePayload`\>(`__namedParameters`): [`BasicGantApi`](../type-aliases/BasicGantApi.md)\<`TEntity`, `TCreatePayload`\>

Defined in: [ui/src/api-client/gantt/base.ts:114](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-client/gantt/base.ts#L114)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### TCreatePayload

`TCreatePayload` = `Omit`\<`TEntity`, `"id"`\>

## Parameters

### \_\_namedParameters

[`ClientGantApiBuilderProps`](../type-aliases/ClientGantApiBuilderProps.md)\<`TEntity`, `TCreatePayload`\>

## Returns

[`BasicGantApi`](../type-aliases/BasicGantApi.md)\<`TEntity`, `TCreatePayload`\>
