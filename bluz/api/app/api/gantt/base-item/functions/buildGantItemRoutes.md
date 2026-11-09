[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/gantt/base-item](../index.md) / buildGantItemRoutes

# Function: buildGantItemRoutes()

> **buildGantItemRoutes**\<`TEntity`, `TCreatePayload`\>(`__namedParameters`): `object`

Defined in: [ui/src/app/api/gantt/base-item.ts:32](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/app/api/gantt/base-item.ts#L32)

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
