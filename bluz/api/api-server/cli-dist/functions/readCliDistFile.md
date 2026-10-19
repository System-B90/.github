[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/cli-dist](../index.md) / readCliDistFile

# Function: readCliDistFile()

> **readCliDistFile**(`name`): `Promise`\<`Buffer`\<`ArrayBufferLike`\> \| `null`\>

Defined in: [ui/src/api-server/cli-dist.ts:38](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/cli-dist.ts#L38)

Bytes of one distributed file, or null. Only names the directory actually
lists are served, so a crafted name can never escape it.

## Parameters

### name

`string`

## Returns

`Promise`\<`Buffer`\<`ArrayBufferLike`\> \| `null`\>
