[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/tls](../index.md) / aiFetch

# Variable: aiFetch

> `const` **aiFetch**: *typeof* `fetch`

Defined in: [ui/src/api-server/ai/tls.ts:90](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/ai/tls.ts#L90)

`fetch` for AI backends: the global one, or undici's with the CA agent when
`AI_CA_CERT_PATH` is set (global fetch cannot take a per-call CA).
