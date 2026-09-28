[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AI\_MAX\_RESPONSE\_TOKENS

# Variable: AI\_MAX\_RESPONSE\_TOKENS

> `const` **AI\_MAX\_RESPONSE\_TOKENS**: `2000` = `2_000`

Defined in: [ui/src/api-shared/types/ai.ts:258](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/types/ai.ts#L258)

Upstream completion cap, sent as `max_tokens` on every model call. Without
it a runaway or adversarial prompt has no ceiling on the bill for a single
response.
