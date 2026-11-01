[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/tls](../index.md) / aiCaAgent

# Function: aiCaAgent()

> **aiCaAgent**(`path?`): `Agent` \| `null`

Defined in: [ui/src/api-server/ai/tls.ts:76](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/ai/tls.ts#L76)

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
