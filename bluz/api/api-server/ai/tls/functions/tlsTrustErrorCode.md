[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/tls](../index.md) / tlsTrustErrorCode

# Function: tlsTrustErrorCode()

> **tlsTrustErrorCode**(`error`): `string` \| `null`

Defined in: [ui/src/api-server/ai/tls.ts:37](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tls.ts#L37)

The TLS trust code behind a failed fetch, if that is what it was. `fetch`
wraps the socket error in `TypeError: fetch failed` with the real one in
`cause` (sometimes nested), so the whole chain is walked.

## Parameters

### error

`unknown`

## Returns

`string` \| `null`
