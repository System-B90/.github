[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / assertWritable

# Variable: assertWritable

> `const` **assertWritable**: (`id?`) => `Promise`\<`void`\> = `assertWritableIteration`

Defined in: [ui/src/api-server/db-iterations.ts:460](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-server/db-iterations.ts#L460)

Guard for write paths: past iterations are reference-only. Throws unless the
resolved iteration is the current one. Omitted id ⇒ current ⇒ writable.

## Parameters

### id?

`string`

## Returns

`Promise`\<`void`\>
