[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / remove

# Variable: remove

> `const` **remove**: (`id`) => `Promise`\<`void`\> = `deleteIteration`

Defined in: [ui/src/api-server/db-iterations.ts:381](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/db-iterations.ts#L381)

Delete an iteration from the registry. Only an orphaned iteration qualifies:
the current one is never deletable (there must always be exactly one writable
iteration), and neither is one that still owns events or a linked curriculum.
The backing Mongo database is left in place — orphaned, not dropped.

## Parameters

### id

`string`

## Returns

`Promise`\<`void`\>
