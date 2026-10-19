[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / isInvalidGrantError

# Function: isInvalidGrantError()

> **isInvalidGrantError**(`error`): `boolean`

Defined in: [ui/src/api-server/google/google-calendar-service.ts:137](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/google/google-calendar-service.ts#L137)

Google's token endpoint refused the refresh token: it expired (7 days on an
OAuth app still in "Testing") or the user revoked access. No retry helps —
only a reconnect does (#914).

## Parameters

### error

`unknown`

## Returns

`boolean`
