[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-cli-handoff](../../../index.md) / [DbCliHandoff](../index.md) / create

# Variable: create

> `const` **create**: (`sessionToken`, `userId`) => `Promise`\<`string`\> = `createHandoffCode`

Defined in: [ui/src/api-server/db-cli-handoff.ts:77](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/db-cli-handoff.ts#L77)

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
