[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / isInvalidGrantError

# Function: isInvalidGrantError()

> **isInvalidGrantError**(`error`): `boolean`

Defined in: [ui/src/api-server/google/google-calendar-service.ts:139](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/google/google-calendar-service.ts#L139)

Google's token endpoint refused the refresh token: it expired (7 days on an
OAuth app still in "Testing") or the user revoked access. No retry helps —
only a reconnect does (#914).

## Parameters

### error

`unknown`

## Returns

`boolean`
