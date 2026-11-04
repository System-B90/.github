[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-outsiders](../../../index.md) / [DbOutsiders](../index.md) / create

# Variable: create

> `const` **create**: (`outsider`, `controller`) => `Promise`\<`Pick`\<[`Outsider`](../../../../../api-shared/types/outsider/type-aliases/Outsider.md), `"id"` \| `"name"` \| `"comment"` \| `"phone"` \| `"personalNumber"` \| `"idNumber"` \| `"releaseDate"`\>\> = `createDbOutsider`

Defined in: [ui/src/api-server/db-outsiders.ts:93](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/db-outsiders.ts#L93)

## Parameters

### outsider

[`Outsider`](../../../../../api-shared/types/outsider/type-aliases/Outsider.md)

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<`Pick`\<[`Outsider`](../../../../../api-shared/types/outsider/type-aliases/Outsider.md), `"id"` \| `"name"` \| `"comment"` \| `"phone"` \| `"personalNumber"` \| `"idNumber"` \| `"releaseDate"`\>\>
