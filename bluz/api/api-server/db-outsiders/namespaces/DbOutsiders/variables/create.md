[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-outsiders](../../../index.md) / [DbOutsiders](../index.md) / create

# Variable: create

> `const` **create**: (`outsider`, `controller`) => `Promise`\<`Pick`\<[`Outsider`](../../../../../api-shared/types/outsider/type-aliases/Outsider.md), `"id"` \| `"name"` \| `"comment"` \| `"phone"` \| `"personalNumber"` \| `"idNumber"` \| `"releaseDate"`\>\> = `createDbOutsider`

Defined in: [ui/src/api-server/db-outsiders.ts:93](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/db-outsiders.ts#L93)

## Parameters

### outsider

[`Outsider`](../../../../../api-shared/types/outsider/type-aliases/Outsider.md)

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<`Pick`\<[`Outsider`](../../../../../api-shared/types/outsider/type-aliases/Outsider.md), `"id"` \| `"name"` \| `"comment"` \| `"phone"` \| `"personalNumber"` \| `"idNumber"` \| `"releaseDate"`\>\>
