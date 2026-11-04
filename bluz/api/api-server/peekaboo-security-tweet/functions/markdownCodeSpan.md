[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/peekaboo-security-tweet](../index.md) / markdownCodeSpan

# Function: markdownCodeSpan()

> **markdownCodeSpan**(`text`): `string`

Defined in: [ui/src/api-server/peekaboo-security-tweet.ts:61](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/peekaboo-security-tweet.ts#L61)

`text` as one inline code span it cannot break out of. The detail is the
attacker's own input (a query string, a request body, a header), so a
plain backtick pair would let it close the span and post live Markdown —
links, `@all` mentions — into the staff channel. CommonMark: a fence longer
than any backtick run inside is never closed early, and Mattermost neither
renders nor notifies mentions inside code.

## Parameters

### text

`string`

## Returns

`string`
