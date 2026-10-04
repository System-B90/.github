[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/base](../index.md) / clientGantApiBuilder

# Function: clientGantApiBuilder()

> **clientGantApiBuilder**\<`TEntity`, `TCreatePayload`\>(`__namedParameters`): [`BasicGantApi`](../type-aliases/BasicGantApi.md)\<`TEntity`, `TCreatePayload`\>

Defined in: [ui/src/api-client/gantt/base.ts:112](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-client/gantt/base.ts#L112)

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
