[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/google-identity](../index.md) / requestGoogleAuthCode

# Function: requestGoogleAuthCode()

> **requestGoogleAuthCode**(`clientId`, `scopes`): `Promise`\<`string`\>

Defined in: [ui/src/api-client/google-identity.ts:59](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-client/google-identity.ts#L59)

Opens the Google consent popup and resolves with the authorization code.
Rejects when the popup is closed/blocked or Google reports an error.

## Parameters

### clientId

`string`

### scopes

`string`[]

## Returns

`Promise`\<`string`\>
