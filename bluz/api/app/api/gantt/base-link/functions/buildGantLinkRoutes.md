[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/gantt/base-link](../index.md) / buildGantLinkRoutes

# Function: buildGantLinkRoutes()

> **buildGantLinkRoutes**\<`TEntity`\>(`__namedParameters`): `object`

Defined in: [ui/src/app/api/gantt/base-link.ts:63](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/app/api/gantt/base-link.ts#L63)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

## Parameters

### \_\_namedParameters

[`BuildGantLinkRoutesProps`](../type-aliases/BuildGantLinkRoutesProps.md)\<`TEntity`\>

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

### POST

> **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

#### Parameters

##### request

`NextRequest`

##### context?

[`RouteContext`](../type-aliases/RouteContext.md)

#### Returns

`Promise`\<`Response`\>
