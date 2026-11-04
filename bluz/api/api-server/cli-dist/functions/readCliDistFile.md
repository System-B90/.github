[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/cli-dist](../index.md) / readCliDistFile

# Function: readCliDistFile()

> **readCliDistFile**(`name`): `Promise`\<`Buffer`\<`ArrayBufferLike`\> \| `null`\>

Defined in: [ui/src/api-server/cli-dist.ts:44](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/cli-dist.ts#L44)

Bytes of one distributed file, or null. Only names the directory actually
lists are served, so a crafted name can never escape it.

## Parameters

### name

`string`

## Returns

`Promise`\<`Buffer`\<`ArrayBufferLike`\> \| `null`\>
