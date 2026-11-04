[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/cli-handoff-rate-limit](../index.md) / rateLimitKeyForRequest

# Function: rateLimitKeyForRequest()

> **rateLimitKeyForRequest**(`request`): `string`

Defined in: [ui/src/api-server/cli-handoff-rate-limit.ts:55](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/cli-handoff-rate-limit.ts#L55)

Best-effort caller identity for rate limiting. Behind the app's own nginx
(see AGENTS.md) `x-real-ip` is `$remote_addr`. The first `x-forwarded-for`
entry is whatever the caller sent, so keying on it let a client mint a
fresh bucket per attempt; the last entry is the one nginx appended. Unset
without a proxy in front, so every direct caller shares one bucket there
rather than the limiter silently doing nothing.

## Parameters

### request

`Request`

## Returns

`string`
