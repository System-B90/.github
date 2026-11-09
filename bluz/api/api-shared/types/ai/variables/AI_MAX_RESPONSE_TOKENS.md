[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AI\_MAX\_RESPONSE\_TOKENS

# Variable: AI\_MAX\_RESPONSE\_TOKENS

> `const` **AI\_MAX\_RESPONSE\_TOKENS**: `2000` = `2_000`

Defined in: [ui/src/api-shared/types/ai.ts:263](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/ai.ts#L263)

Upstream completion cap, sent as `max_tokens` on every model call. Without
it a runaway or adversarial prompt has no ceiling on the bill for a single
response.
