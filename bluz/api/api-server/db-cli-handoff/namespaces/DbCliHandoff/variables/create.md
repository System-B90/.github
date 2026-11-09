[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-cli-handoff](../../../index.md) / [DbCliHandoff](../index.md) / create

# Variable: create

> `const` **create**: (`sessionToken`, `userId`) => `Promise`\<`string`\> = `createHandoffCode`

Defined in: [ui/src/api-server/db-cli-handoff.ts:83](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/db-cli-handoff.ts#L83)

Mint a handoff code bound to `userId`, sealing `sessionToken` at rest
(secret-box.ts) rather than storing it in the clear.

## Parameters

### sessionToken

`string`

### userId

`string`

## Returns

`Promise`\<`string`\>

The opaque handoff code to hand the browser (never the token).
