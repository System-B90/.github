[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/peekaboo-security-tweet](../index.md) / markdownCodeSpan

# Function: markdownCodeSpan()

> **markdownCodeSpan**(`text`): `string`

Defined in: [ui/src/api-server/peekaboo-security-tweet.ts:51](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-server/peekaboo-security-tweet.ts#L51)

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
