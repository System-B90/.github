[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/common/UseEntityForm](../index.md) / useEntityForm

# Function: useEntityForm()

> **useEntityForm**\<`TEntity`, `TValues`\>(`__namedParameters`): `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx:82](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/settings-dialog/tabs/global/common/UseEntityForm.tsx#L82)

The "list + form" state every settings tab was re-implementing: which entity
is selected, whether we are creating, one value bag, and the
populate / start-create / cancel / save / delete handlers around it —
including the validate-then-snackbar and the error snackbar on failure.

Extracted from the outsider and room tabs, which had this same shape spelled
out field by field (see #191). Keeping it in one place also means the tabs
pass a single `form` object to their FormCard instead of drilling every
value and setter as its own prop.

## Type Parameters

### TEntity

`TEntity` *extends* `object`

### TValues

`TValues`

## Parameters

### \_\_namedParameters

[`UseEntityFormProps`](../type-aliases/UseEntityFormProps.md)\<`TEntity`, `TValues`\>

## Returns

### clearForm

> **clearForm**: () => `void`

Empties the form without asking — after a save or a delete.

#### Returns

`void`

### confirmDialog

> **confirmDialog**: `Element`

### errors

> **errors**: `Partial`\<`Record`\<keyof `TValues`, `string`\>\>

### handleCancelEdit

> **handleCancelEdit**: () => `void`

#### Returns

`void`

### handleDelete

> **handleDelete**: (`id`) => `Promise`\<`void`\>

#### Parameters

##### id

`string`

#### Returns

`Promise`\<`void`\>

### handleSave

> **handleSave**: (`event`) => `Promise`\<`void`\>

#### Parameters

##### event

`FormEvent`

#### Returns

`Promise`\<`void`\>

### handleStartCreate

> **handleStartCreate**: () => `void`

#### Returns

`void`

### isCreating

> **isCreating**: `boolean`

### isDirty

> **isDirty**: `boolean`

### isSubmitting

> **isSubmitting**: `boolean`

### populateFormFrom

> **populateFormFrom**: (`entity`) => `void`

#### Parameters

##### entity

`TEntity`

#### Returns

`void`

### populateFormState

> **populateFormState**: (`entity`) => `void`

Loads an entity into the form. Does not notify `onSelectionChange` —
callers that sync a URL param drive that themselves, so restoring a
selection *from* the URL doesn't write it straight back.

#### Parameters

##### entity

`TEntity`

#### Returns

`void`

### selectedEntity

> **selectedEntity**: `TEntity` \| `null`

### setValue

> **setValue**: \<`TKey`\>(`key`, `value`) => `void`

Updates one field, leaving the rest untouched, and clears its error.

#### Type Parameters

##### TKey

`TKey` *extends* `string` \| `number` \| `symbol`

#### Parameters

##### key

`TKey`

##### value

`TValues`\[`TKey`\]

#### Returns

`void`

### setValues

> **setValues**: `Dispatch`\<`SetStateAction`\<`TValues`\>\>

### values

> **values**: `TValues`
