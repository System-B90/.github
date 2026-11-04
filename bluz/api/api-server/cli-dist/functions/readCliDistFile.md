[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/cli-dist](../index.md) / readCliDistFile

# Function: readCliDistFile()

> **readCliDistFile**(`name`): `Promise`\<`Buffer`\<`ArrayBufferLike`\> \| `null`\>

Defined in: [ui/src/api-server/cli-dist.ts:44](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/cli-dist.ts#L44)

Bytes of one distributed file, or null. Only names the directory actually
lists are served, so a crafted name can never escape it.

## Parameters

### name

`string`

## Returns

`Promise`\<`Buffer`\<`ArrayBufferLike`\> \| `null`\>
