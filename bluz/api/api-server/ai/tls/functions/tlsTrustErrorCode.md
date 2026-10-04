[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/tls](../index.md) / tlsTrustErrorCode

# Function: tlsTrustErrorCode()

> **tlsTrustErrorCode**(`error`): `string` \| `null`

Defined in: [ui/src/api-server/ai/tls.ts:37](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/tls.ts#L37)

The TLS trust code behind a failed fetch, if that is what it was. `fetch`
wraps the socket error in `TypeError: fetch failed` with the real one in
`cause` (sometimes nested), so the whole chain is walked.

## Parameters

### error

`unknown`

## Returns

`string` \| `null`
