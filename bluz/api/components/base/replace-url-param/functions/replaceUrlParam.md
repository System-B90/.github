[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/replace-url-param](../index.md) / replaceUrlParam

# Function: replaceUrlParam()

> **replaceUrlParam**(`name`, `value`): `void`

Defined in: [ui/src/components/base/replace-url-param.ts:7](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/replace-url-param.ts#L7)

Sets `name` in the address bar's query to `value`, or removes it for
`null`, without a navigation or a history entry. Keeps `history.state`:
Next's router stores its own entry there, and replacing it with `null`
broke Back/Forward out of the page.

## Parameters

### name

`string`

### value

`string` \| `null`

## Returns

`void`
