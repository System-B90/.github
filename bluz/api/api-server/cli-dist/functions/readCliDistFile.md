[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/cli-dist](../index.md) / readCliDistFile

# Function: readCliDistFile()

> **readCliDistFile**(`name`): `Promise`\<`Buffer`\<`ArrayBufferLike`\> \| `null`\>

Defined in: [ui/src/api-server/cli-dist.ts:44](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/cli-dist.ts#L44)

Bytes of one distributed file, or null. Only names the directory actually
lists are served, so a crafted name can never escape it.

## Parameters

### name

`string`

## Returns

`Promise`\<`Buffer`\<`ArrayBufferLike`\> \| `null`\>
