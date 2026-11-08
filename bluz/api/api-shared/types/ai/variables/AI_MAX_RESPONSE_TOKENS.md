[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AI\_MAX\_RESPONSE\_TOKENS

# Variable: AI\_MAX\_RESPONSE\_TOKENS

> `const` **AI\_MAX\_RESPONSE\_TOKENS**: `2000` = `2_000`

Defined in: [ui/src/api-shared/types/ai.ts:263](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types/ai.ts#L263)

Upstream completion cap, sent as `max_tokens` on every model call. Without
it a runaway or adversarial prompt has no ceiling on the bill for a single
response.
