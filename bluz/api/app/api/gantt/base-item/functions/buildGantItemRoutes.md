[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/gantt/base-item](../index.md) / buildGantItemRoutes

# Function: buildGantItemRoutes()

> **buildGantItemRoutes**\<`TEntity`, `TCreatePayload`\>(`__namedParameters`): `object`

Defined in: [ui/src/app/api/gantt/base-item.ts:30](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/app/api/gantt/base-item.ts#L30)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### TCreatePayload

`TCreatePayload` = `Omit`\<`TEntity`, `"id"`\>

## Parameters

### \_\_namedParameters

[`BuildGantItemRoutesProps`](../type-aliases/BuildGantItemRoutesProps.md)\<`TEntity`, `TCreatePayload`\>

## Returns

`object`

### DELETE

> **DELETE**: (`request`, `context?`) => `Promise`\<`Response`\>

#### Parameters

##### request

`NextRequest`

##### context?

[`RouteContext`](../type-aliases/RouteContext.md)

#### Returns

`Promise`\<`Response`\>

### GET

> **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

#### Parameters

##### request

`NextRequest`

##### context?

[`RouteContext`](../type-aliases/RouteContext.md)

#### Returns

`Promise`\<`Response`\>

### PATCH

> **PATCH**: (`request`, `context?`) => `Promise`\<`Response`\>

#### Parameters

##### request

`NextRequest`

##### context?

[`RouteContext`](../type-aliases/RouteContext.md)

#### Returns

`Promise`\<`Response`\>
