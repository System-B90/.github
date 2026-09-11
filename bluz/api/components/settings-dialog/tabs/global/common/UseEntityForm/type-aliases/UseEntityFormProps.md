[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/common/UseEntityForm](../index.md) / UseEntityFormProps

# Type Alias: UseEntityFormProps\<TEntity, TValues\>

> **UseEntityFormProps**\<`TEntity`, `TValues`\> = `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:14](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L14)

## Type Parameters

### TEntity

`TEntity`

### TValues

`TValues`

## Properties

### confirmDeleteMessage?

> `optional` **confirmDeleteMessage?**: (`id`) => `string`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:47](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L47)

Builds the delete confirmation prompt for a given id.

#### Parameters

##### id

`string`

#### Returns

`string`

***

### emptyValues

> **emptyValues**: `TValues`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L16)

Blank form — used for "create new" and for clearing after save/cancel.

***

### errorMessages

> **errorMessages**: `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:41](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L41)

Error snackbar titles, e.g. `{ create: "שגיאה ביצירת איש חוץ" }`.

#### create

> **create**: `string`

#### delete?

> `optional` **delete?**: `string`

#### update

> **update**: `string`

***

### keepSelectionAfterSave?

> `optional` **keepSelectionAfterSave?**: `boolean`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:39](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L39)

By default a successful save clears the form, which is what a
list-and-add tab wants. Set this to keep the saved entity selected and
the form populated from whatever `onCreate`/`onUpdate` returned — for
tabs where saving is "apply my edits", not "add another".

***

### onCreate

> **onCreate**: (`values`) => `Promise`\<`TEntity` \| `unknown`\>

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:30](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L30)

Returning the saved entity lets `keepSelectionAfterSave` re-populate the
form from the server's version. Returning nothing is fine otherwise.

#### Parameters

##### values

`TValues`

#### Returns

`Promise`\<`TEntity` \| `unknown`\>

***

### onDelete?

> `optional` **onDelete?**: (`id`) => `Promise`\<`unknown`\>

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:32](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L32)

#### Parameters

##### id

`string`

#### Returns

`Promise`\<`unknown`\>

***

### onSelectionChange?

> `optional` **onSelectionChange?**: (`entityId`) => `void`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:49](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L49)

Runs after the selection changes, e.g. to sync a URL query param.

#### Parameters

##### entityId

`null` \| `string`

#### Returns

`void`

***

### onUpdate

> **onUpdate**: (`entity`, `values`) => `Promise`\<`TEntity` \| `unknown`\>

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:31](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L31)

#### Parameters

##### entity

`TEntity`

##### values

`TValues`

#### Returns

`Promise`\<`TEntity` \| `unknown`\>

***

### toValues

> **toValues**: (`entity`) => `TValues`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:18](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L18)

Fills the form when an existing entity is selected for editing.

#### Parameters

##### entity

`TEntity`

#### Returns

`TValues`

***

### validate

> **validate**: (`values`) => [`ValidationResult`](ValidationResult.md)

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L25)

Checked before any request. Return the warning to show, or `null` to
proceed. Trimming belongs here or in `onCreate`/`onUpdate` — the hook
deliberately does not trim, since which fields are strings is the
caller's business.

#### Parameters

##### values

`TValues`

#### Returns

[`ValidationResult`](ValidationResult.md)
