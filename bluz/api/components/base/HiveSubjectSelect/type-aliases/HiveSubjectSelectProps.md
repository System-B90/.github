[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/HiveSubjectSelect](../index.md) / HiveSubjectSelectProps

# Type Alias: HiveSubjectSelectProps

> **HiveSubjectSelectProps** = `object` & `Omit`\<`FormControlProps`, `"onChange"`\>

Defined in: [ui/src/components/base/HiveSubjectSelect.tsx:6](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/HiveSubjectSelect.tsx#L6)

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
