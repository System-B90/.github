[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/HiveLessonSelect](../index.md) / HiveLessonSelectProps

# Type Alias: HiveLessonSelectProps

> **HiveLessonSelectProps** = `object` & `Omit`\<`FormControlProps`, `"onChange"`\>

Defined in: [ui/src/components/base/HiveLessonSelect.tsx:7](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/HiveLessonSelect.tsx#L7)

## Type Declaration

### allowEmpty?

> `optional` **allowEmpty?**: `boolean`

Render a leading empty option so the user can clear the choice.

### emptyLabel?

> `optional` **emptyLabel?**: `string`

Label for the empty option.

### label?

> `optional` **label?**: `string`

Field label. Defaults to the Hebrew "שיעור".

### module?

> `optional` **module?**: `null` \| `number` \| `string`

Scope the options to a single module. When omitted, every lesson is
offered. Passing a module enables cascading module → lesson picking.

### onChange

> **onChange**: (`lessonId`) => `void`

Fired with the picked lesson id, or null when cleared.

#### Parameters

##### lessonId

`null` \| `number`

#### Returns

`void`

### value

> **value**: `null` \| `number`

Selected lesson id (controlled). Use null for no selection.
