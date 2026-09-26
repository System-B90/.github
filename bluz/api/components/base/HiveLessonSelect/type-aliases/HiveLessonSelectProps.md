[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/HiveLessonSelect](../index.md) / HiveLessonSelectProps

# Type Alias: HiveLessonSelectProps

> **HiveLessonSelectProps** = `object` & `Omit`\<`FormControlProps`, `"onChange"`\>

Defined in: [ui/src/components/base/HiveLessonSelect.tsx:8](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/HiveLessonSelect.tsx#L8)

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

[`HiveLessonId`](../../../../api-shared/types/hive/type-aliases/HiveLessonId.md) \| `null`

#### Returns

`void`

### value

> **value**: [`HiveLessonId`](../../../../api-shared/types/hive/type-aliases/HiveLessonId.md) \| `null`

Selected lesson id (controlled). Use null for no selection.
