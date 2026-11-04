[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / assertWritable

# Variable: assertWritable

> `const` **assertWritable**: (`id?`) => `Promise`\<`void`\> = `assertWritableIteration`

Defined in: [ui/src/api-server/db-iterations.ts:460](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/db-iterations.ts#L460)

Guard for write paths: past iterations are reference-only. Throws unless the
resolved iteration is the current one. Omitted id ⇒ current ⇒ writable.

## Parameters

### id?

`string`

## Returns

`Promise`\<`void`\>
