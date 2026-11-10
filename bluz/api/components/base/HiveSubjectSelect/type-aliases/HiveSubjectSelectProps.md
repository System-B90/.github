[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/HiveSubjectSelect](../index.md) / HiveSubjectSelectProps

# Type Alias: HiveSubjectSelectProps

> **HiveSubjectSelectProps** = `object` & `Omit`\<`FormControlProps`, `"onChange"`\>

Defined in: [ui/src/components/base/HiveSubjectSelect.tsx:6](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/base/HiveSubjectSelect.tsx#L6)

## Type Declaration

### allowEmpty?

> `optional` **allowEmpty?**: `boolean`

Render a leading empty option so the user can clear the choice.

### emptyLabel?

> `optional` **emptyLabel?**: `string`

Label for the empty option.

### label?

> `optional` **label?**: `string`

Field label. Defaults to the Hebrew "מקצוע".

### onChange

> **onChange**: (`subjectId`) => `void`

Fired with the picked subject id, or null when cleared.

#### Parameters

##### subjectId

`null` \| `string`

#### Returns

`void`

### value

> **value**: `null` \| `string`

Selected subject id (controlled). Use null/"" for no selection.
