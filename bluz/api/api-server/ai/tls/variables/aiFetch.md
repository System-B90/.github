[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/tls](../index.md) / aiFetch

# Variable: aiFetch

> `const` **aiFetch**: *typeof* `fetch`

Defined in: [ui/src/api-server/ai/tls.ts:90](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/api-server/ai/tls.ts#L90)

`fetch` for AI backends: the global one, or undici's with the CA agent when
`AI_CA_CERT_PATH` is set (global fetch cannot take a per-call CA).
