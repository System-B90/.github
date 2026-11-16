[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/tls](../index.md) / tlsTrustErrorCode

# Function: tlsTrustErrorCode()

> **tlsTrustErrorCode**(`error`): `string` \| `null`

Defined in: [ui/src/api-server/ai/tls.ts:37](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-server/ai/tls.ts#L37)

The TLS trust code behind a failed fetch, if that is what it was. `fetch`
wraps the socket error in `TypeError: fetch failed` with the real one in
`cause` (sometimes nested), so the whole chain is walked.

## Parameters

### error

`unknown`

## Returns

`string` \| `null`
