[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/cli-handoff-rate-limit](../index.md) / rateLimitKeyForRequest

# Function: rateLimitKeyForRequest()

> **rateLimitKeyForRequest**(`request`): `string`

Defined in: [ui/src/api-server/cli-handoff-rate-limit.ts:42](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/cli-handoff-rate-limit.ts#L42)

Best-effort caller identity for rate limiting. Behind the app's own nginx
(see AGENTS.md) `x-forwarded-for` carries the real client IP; unset in
environments without a proxy in front, so every direct caller shares one
bucket there rather than the limiter silently doing nothing.

## Parameters

### request

`Request`

## Returns

`string`
