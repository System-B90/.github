[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / isInvalidGrantError

# Function: isInvalidGrantError()

> **isInvalidGrantError**(`error`): `boolean`

Defined in: [ui/src/api-server/google/google-calendar-service.ts:137](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/google/google-calendar-service.ts#L137)

Google's token endpoint refused the refresh token: it expired (7 days on an
OAuth app still in "Testing") or the user revoked access. No retry helps —
only a reconnect does (#914).

## Parameters

### error

`unknown`

## Returns

`boolean`
