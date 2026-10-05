[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-base](../index.md) / drizzleOperationsBuilder

# Function: drizzleOperationsBuilder()

> **drizzleOperationsBuilder**\<`T`, `TTable`, `TCreatePayload`\>(`__namedParameters`): `Omit`\<[`BasicGantOperations`](../../../../api-shared/types/gantt/api-layer/type-aliases/BasicGantOperations.md)\<`T`, `TCreatePayload`\>, `"createNewItem"` \| `"getItem"` \| `"updateItem"`\> & `object`

Defined in: [ui/src/api-server/gantt/db-base.ts:231](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/gantt/db-base.ts#L231)

## Type Parameters

### T

`T` *extends* [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### TTable

`TTable` *extends* `PgTableWithColumns`\<`any`\>

### TCreatePayload

`TCreatePayload` = `Omit`\<`T`, `"id"`\>

## Parameters

### \_\_namedParameters

[`DrizzleOperationsBuilderProps`](../type-aliases/DrizzleOperationsBuilderProps.md)\<`TTable`\>

## Returns
