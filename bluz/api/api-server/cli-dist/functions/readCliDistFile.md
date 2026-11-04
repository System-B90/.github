[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/cli-dist](../index.md) / readCliDistFile

# Function: readCliDistFile()

> **readCliDistFile**(`name`): `Promise`\<`Buffer`\<`ArrayBufferLike`\> \| `null`\>

Defined in: [ui/src/api-server/cli-dist.ts:44](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/cli-dist.ts#L44)

Bytes of one distributed file, or null. Only names the directory actually
lists are served, so a crafted name can never escape it.

## Parameters

### name

`string`

## Returns

`Promise`\<`Buffer`\<`ArrayBufferLike`\> \| `null`\>
