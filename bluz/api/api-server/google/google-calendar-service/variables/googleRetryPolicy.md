[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / googleRetryPolicy

# Variable: googleRetryPolicy

> `const` **googleRetryPolicy**: `object`

Defined in: [ui/src/api-server/google/google-calendar-service.ts:110](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/google/google-calendar-service.ts#L110)

Retry policy for Calendar API calls. Mutable so tests can zero the delays;
production keeps Google's recommended truncated exponential backoff.

## Type Declaration

### attempts

> **attempts**: `number` = `4`

Total attempts, including the first.

### baseDelayMs

> **baseDelayMs**: `number` = `500`

### maxDelayMs

> **maxDelayMs**: `number` = `8_000`
