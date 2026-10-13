[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/tls](../index.md) / aiFetch

# Variable: aiFetch

> `const` **aiFetch**: *typeof* `fetch`

Defined in: [ui/src/api-server/ai/tls.ts:85](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/ai/tls.ts#L85)

`fetch` for AI backends: the global one, or undici's with the CA agent when
`AI_CA_CERT_PATH` is set (global fetch cannot take a per-call CA).
