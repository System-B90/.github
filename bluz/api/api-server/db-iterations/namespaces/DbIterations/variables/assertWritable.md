[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / assertWritable

# Variable: assertWritable

> `const` **assertWritable**: (`id?`) => `Promise`\<`void`\> = `assertWritableIteration`

Defined in: [ui/src/api-server/db-iterations.ts:385](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/db-iterations.ts#L385)

Guard for write paths: past iterations are reference-only. Throws unless the
resolved iteration is the current one. Omitted id ⇒ current ⇒ writable.

## Parameters

### id?

`string`

## Returns

`Promise`\<`void`\>
