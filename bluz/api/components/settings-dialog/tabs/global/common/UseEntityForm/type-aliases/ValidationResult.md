[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/common/UseEntityForm](../index.md) / ValidationResult

# Type Alias: ValidationResult\<TValues\>

> **ValidationResult**\<`TValues`\> = [`FieldError`](FieldError.md)\<`TValues`\> \| `null` \| `string`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:20](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L20)

A validation failure. A `FieldError` is shown on its field, which gets
focus; a bare string (no single field to blame) is a warning snackbar.
Returning `null` means the values are valid.

## Type Parameters

### TValues

`TValues`
