[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/outsider-settings/values](../index.md) / outsiderValuesToPayload

# Function: outsiderValuesToPayload()

> **outsiderValuesToPayload**(`values`): `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/outsider-settings/values.ts:58](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/settings-dialog/tabs/global/outsider-settings/values.ts#L58)

Maps the form values onto the API payload, trimming blanks to `null`.

`null` rather than `undefined` on purpose: the server applies the payload
as a plain `$set`, and `JSON.stringify` drops `undefined` keys entirely, so
a field the user cleared would silently keep its old value on the server.

## Parameters

### values

[`OutsiderValues`](../type-aliases/OutsiderValues.md)

## Returns

`object`

### comment

> **comment**: `string` \| `null`

### idNumber

> **idNumber**: `string` \| `null`

### name

> **name**: `string`

### personalNumber

> **personalNumber**: `string` \| `null`

### phone

> **phone**: `string`

### releaseDate

> **releaseDate**: `string` \| `null`
