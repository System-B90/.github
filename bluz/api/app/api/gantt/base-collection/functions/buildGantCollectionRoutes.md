[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/gantt/base-collection](../index.md) / buildGantCollectionRoutes

# Function: buildGantCollectionRoutes()

> **buildGantCollectionRoutes**\<`TEntity`, `TCreatePayload`\>(`__namedParameters`): `object`

Defined in: [ui/src/app/api/gantt/base-collection.ts:29](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/app/api/gantt/base-collection.ts#L29)

## Type Parameters

### TEntity

`TEntity` *extends* [`BaseGantItem`](../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

### TCreatePayload

`TCreatePayload` = `Omit`\<`TEntity`, `"id"`\>

## Parameters

### \_\_namedParameters

[`BuildGantCollectionRoutesProps`](../type-aliases/BuildGantCollectionRoutesProps.md)\<`TEntity`, `TCreatePayload`\>

## Returns

`object`

### GET

> **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

#### Parameters

##### request

`NextRequest`

##### context?

`any`

#### Returns

`Promise`\<`Response`\>

### POST

> **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

#### Parameters

##### request

`NextRequest`

##### context?

`any`

#### Returns

`Promise`\<`Response`\>
