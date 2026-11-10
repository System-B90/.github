[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/common/UseEntityForm](../index.md) / ValidationResult

# Type Alias: ValidationResult\<TValues\>

> **ValidationResult**\<`TValues`\> = [`FieldError`](FieldError.md)\<`TValues`\> \| `null` \| `string`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:20](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L20)

A validation failure. A `FieldError` is shown on its field, which gets
focus; a bare string (no single field to blame) is a warning snackbar.
Returning `null` means the values are valid.

## Type Parameters

### TValues

`TValues`
