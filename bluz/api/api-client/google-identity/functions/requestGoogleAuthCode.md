[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/google-identity](../index.md) / requestGoogleAuthCode

# Function: requestGoogleAuthCode()

> **requestGoogleAuthCode**(`clientId`, `scopes`): `Promise`\<`string`\>

Defined in: [ui/src/api-client/google-identity.ts:55](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-client/google-identity.ts#L55)

Opens the Google consent popup and resolves with the authorization code.
Rejects when the popup is closed/blocked or Google reports an error.

## Parameters

### clientId

`string`

### scopes

`string`[]

## Returns

`Promise`\<`string`\>
