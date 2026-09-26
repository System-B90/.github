[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/gantt/base-allocate-time](../index.md) / buildGantAllocateTimeRoutes

# Function: buildGantAllocateTimeRoutes()

> **buildGantAllocateTimeRoutes**\<`TEntity`\>(`__namedParameters`): `object`

Defined in: [ui/src/app/api/gantt/base-allocate-time.ts:43](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/app/api/gantt/base-allocate-time.ts#L43)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

## Parameters

### \_\_namedParameters

[`BuildGantAllocateTimeRoutesProps`](../type-aliases/BuildGantAllocateTimeRoutesProps.md)\<`TEntity`\>

## Returns

`object`

### GET

> **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

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
