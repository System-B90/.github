[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / remove

# Variable: remove

> `const` **remove**: (`id`) => `Promise`\<`void`\> = `deleteIteration`

Defined in: [ui/src/api-server/db-iterations.ts:383](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/db-iterations.ts#L383)

Delete an iteration from the registry. Only an orphaned iteration qualifies:
the current one is never deletable (there must always be exactly one writable
iteration), and neither is one that still owns events or a linked curriculum.
The backing Mongo database is left in place — orphaned, not dropped.

## Parameters

### id

`string`

## Returns

`Promise`\<`void`\>
