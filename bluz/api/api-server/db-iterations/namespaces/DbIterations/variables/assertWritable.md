[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / assertWritable

# Variable: assertWritable

> `const` **assertWritable**: (`id?`) => `Promise`\<`void`\> = `assertWritableIteration`

Defined in: [ui/src/api-server/db-iterations.ts:460](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-server/db-iterations.ts#L460)

Guard for write paths: past iterations are reference-only. Throws unless the
resolved iteration is the current one. Omitted id ⇒ current ⇒ writable.

## Parameters

### id?

`string`

## Returns

`Promise`\<`void`\>
