[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AI\_MAX\_RESPONSE\_TOKENS

# Variable: AI\_MAX\_RESPONSE\_TOKENS

> `const` **AI\_MAX\_RESPONSE\_TOKENS**: `2000` = `2_000`

Defined in: [ui/src/api-shared/types/ai.ts:263](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/ai.ts#L263)

Upstream completion cap, sent as `max_tokens` on every model call. Without
it a runaway or adversarial prompt has no ceiling on the bill for a single
response.
