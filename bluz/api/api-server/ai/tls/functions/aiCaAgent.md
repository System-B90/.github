[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/tls](../index.md) / aiCaAgent

# Function: aiCaAgent()

> **aiCaAgent**(`path?`): `Agent` \| `null`

Defined in: [ui/src/api-server/ai/tls.ts:72](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tls.ts#L72)

An undici agent trusting the system roots plus `AI_CA_CERT_PATH`, or null
when the variable is unset. Built once per path.

## Parameters

### path?

`string` \| `undefined`

## Returns

`Agent` \| `null`

## Throws

When the file cannot be read: a set-but-broken CA path is a
misconfiguration worth failing loudly on, not silently ignoring.
