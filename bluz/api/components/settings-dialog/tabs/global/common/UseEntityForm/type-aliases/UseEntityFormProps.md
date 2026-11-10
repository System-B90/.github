[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/common/UseEntityForm](../index.md) / UseEntityFormProps

# Type Alias: UseEntityFormProps\<TEntity, TValues\>

> **UseEntityFormProps**\<`TEntity`, `TValues`\> = `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:25](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L25)

## Type Parameters

### TEntity

`TEntity`

### TValues

`TValues`

## Properties

### confirmDelete?

> `optional` **confirmDelete?**: `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:63](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L63)

The delete confirmation: its title, and the prompt for a given id.
Omitted → deletes without asking.

#### message

> **message**: (`id`) => `string`

##### Parameters

###### id

`string`

##### Returns

`string`

#### title

> **title**: `string`

***

### emptyValues

> **emptyValues**: `TValues`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:27](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L27)

Blank form — used for "create new" and for clearing after save/cancel.

***

### errorMessages

> **errorMessages**: `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:54](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L54)

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

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:52](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L52)

By default a successful save clears the form, which is what a
list-and-add tab wants. Set this to keep the saved entity selected and
the form populated from whatever `onCreate`/`onUpdate` returned — for
tabs where saving is "apply my edits", not "add another".

***

### onCreate

> **onCreate**: (`values`) => `Promise`\<`TEntity` \| `unknown`\>

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:43](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L43)

Returning the saved entity lets `keepSelectionAfterSave` re-populate the
form from the server's version. Returning nothing is fine otherwise.
Returning `false` means the save failed and was already reported: the
form keeps what was typed.

#### Parameters

##### values

`TValues`

#### Returns

`Promise`\<`TEntity` \| `unknown`\>

***

### onDelete?

> `optional` **onDelete?**: (`id`) => `Promise`\<`unknown`\>

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:45](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L45)

#### Parameters

##### id

`string`

#### Returns

`Promise`\<`unknown`\>

***

### onSelectionChange?

> `optional` **onSelectionChange?**: (`entityId`) => `void`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:68](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L68)

Runs after the selection changes, e.g. to sync a URL query param.

#### Parameters

##### entityId

`null` \| `string`

#### Returns

`void`

***

### onUpdate

> **onUpdate**: (`entity`, `values`) => `Promise`\<`TEntity` \| `unknown`\>

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:44](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L44)

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

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:29](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L29)

Fills the form when an existing entity is selected for editing.

#### Parameters

##### entity

`TEntity`

#### Returns

`TValues`

***

### validate

> **validate**: (`values`) => [`ValidationResult`](ValidationResult.md)\<`TValues`\>

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:36](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L36)

Checked before any request. Return the warning to show, or `null` to
proceed. Trimming belongs here or in `onCreate`/`onUpdate` — the hook
deliberately does not trim, since which fields are strings is the
caller's business.

#### Parameters

##### values

`TValues`

#### Returns

[`ValidationResult`](ValidationResult.md)\<`TValues`\>
