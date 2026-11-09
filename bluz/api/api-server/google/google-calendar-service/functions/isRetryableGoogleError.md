[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / isRetryableGoogleError

# Function: isRetryableGoogleError()

> **isRetryableGoogleError**(`error`): `boolean`

Defined in: [ui/src/api-server/google/google-calendar-service.ts:161](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/google/google-calendar-service.ts#L161)

Per Google's error guide: back off on 429, 5xx and the two 403 rate-limit
reasons; never on other 4xx (400/401/403-forbidden/404/409/410/412), which
the caller must handle semantically.

## Parameters

### error

`unknown`

## Returns

`boolean`
