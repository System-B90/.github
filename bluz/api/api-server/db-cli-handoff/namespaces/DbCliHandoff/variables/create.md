[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-cli-handoff](../../../index.md) / [DbCliHandoff](../index.md) / create

# Variable: create

> `const` **create**: (`sessionToken`, `userId`) => `Promise`\<`string`\> = `createHandoffCode`

Defined in: [ui/src/api-server/db-cli-handoff.ts:77](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/db-cli-handoff.ts#L77)

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
