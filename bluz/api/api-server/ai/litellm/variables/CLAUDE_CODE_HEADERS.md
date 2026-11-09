[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/litellm](../index.md) / CLAUDE\_CODE\_HEADERS

# Variable: CLAUDE\_CODE\_HEADERS

> `const` **CLAUDE\_CODE\_HEADERS**: `Readonly`\<`Record`\<`string`, `string`\>\>

Defined in: [ui/src/api-server/ai/litellm.ts:26](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/ai/litellm.ts#L26)

What Claude Code sends with every request to `ANTHROPIC_BASE_URL`. The
version in the User-Agent only has to look like Claude Code's; override it
(or anything else) with `ANTHROPIC_CUSTOM_HEADERS`.
