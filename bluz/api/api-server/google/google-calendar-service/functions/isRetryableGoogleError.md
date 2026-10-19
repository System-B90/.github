[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / isRetryableGoogleError

# Function: isRetryableGoogleError()

> **isRetryableGoogleError**(`error`): `boolean`

Defined in: [ui/src/api-server/google/google-calendar-service.ts:157](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/google/google-calendar-service.ts#L157)

Per Google's error guide: back off on 429, 5xx and the two 403 rate-limit
reasons; never on other 4xx (400/401/403-forbidden/404/409/410/412), which
the caller must handle semantically.

## Parameters

### error

`unknown`

## Returns

`boolean`
