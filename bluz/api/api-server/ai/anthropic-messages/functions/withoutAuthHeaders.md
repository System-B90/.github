[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/anthropic-messages](../index.md) / withoutAuthHeaders

# Function: withoutAuthHeaders()

> **withoutAuthHeaders**(`headers`, `provider`): `Record`\<`string`, `string`\>

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:194](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/ai/anthropic-messages.ts#L194)

`headers` without credential headers. One in `ANTHROPIC_CUSTOM_HEADERS`
(e.g. a Claude Code `ANTHROPIC_AUTH_TOKEN` carried over as a header) used
to replace the selected key, so a personal `sk-` token reached LiteLLM as
an SSO JWT. Dropping it by name, case-insensitively, also stops `fetch`
from joining `authorization` and `Authorization` into one value.

## Parameters

### headers

`Readonly`\<`Record`\<`string`, `string`\>\>

### provider

`string`

## Returns

`Record`\<`string`, `string`\>
