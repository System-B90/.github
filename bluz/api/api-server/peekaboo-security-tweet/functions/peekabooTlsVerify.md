[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/peekaboo-security-tweet](../index.md) / peekabooTlsVerify

# Function: peekabooTlsVerify()

> **peekabooTlsVerify**(`value?`): `boolean`

Defined in: [ui/src/api-server/peekaboo-security-tweet.ts:26](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/peekaboo-security-tweet.ts#L26)

Peek-a-Boo usually sits behind an internal, self-signed certificate, and an
alert that dies on a TLS handshake is worse than none: certificate checks
are off for this one destination only, whatever NODE_TLS_REJECT_UNAUTHORIZED
says for the rest of the process. `PEEKABOO_TLS_VERIFY=true` turns them back
on for deployments where Peek-a-Boo has a trusted certificate.

## Parameters

### value?

`string` \| `undefined`

## Returns

`boolean`
