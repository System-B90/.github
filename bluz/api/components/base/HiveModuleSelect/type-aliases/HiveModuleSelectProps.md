[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/HiveModuleSelect](../index.md) / HiveModuleSelectProps

# Type Alias: HiveModuleSelectProps

> **HiveModuleSelectProps** = `object` & `Omit`\<`FormControlProps`, `"onChange"`\>

Defined in: [ui/src/components/base/HiveModuleSelect.tsx:8](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/base/HiveModuleSelect.tsx#L8)

## Type Declaration

### allowEmpty?

> `optional` **allowEmpty?**: `boolean`

Render a leading empty option so the user can clear the choice.

### autoSelectSole?

> `optional` **autoSelectSole?**: `boolean`

Pick the option automatically when it is the only one.

### emptyLabel?

> `optional` **emptyLabel?**: `string`

Label for the empty option.

### label?

> `optional` **label?**: `string`

Field label. Defaults to the Hebrew "מערך".

### onChange

> **onChange**: (`moduleId`) => `void`

Fired with the picked module id, or null when cleared.

#### Parameters

##### moduleId

`null` \| `string`

#### Returns

`void`

### subject?

> `optional` **subject?**: [`SubjectLike`](../../../../api-shared/types/subject/type-aliases/SubjectLike.md)

Scope the options to a single subject. When omitted, every module is
offered. Passing a subject enables cascading subject → module picking.

### value

> **value**: `null` \| `string`

Selected module id (controlled). Use null/"" for no selection.
