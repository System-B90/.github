[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/replace-url-param](../index.md) / replaceUrlParam

# Function: replaceUrlParam()

> **replaceUrlParam**(`name`, `value`): `void`

Defined in: [ui/src/components/base/replace-url-param.ts:7](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/base/replace-url-param.ts#L7)

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
