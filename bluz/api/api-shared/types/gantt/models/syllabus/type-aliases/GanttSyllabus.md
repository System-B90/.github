[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/syllabus](../index.md) / GanttSyllabus

# Type Alias: GanttSyllabus

> **GanttSyllabus** = `object` & [`BaseGantItem`](../../shared/type-aliases/BaseGantItem.md)

Defined in: [ui/src/api-shared/types/gantt/models/syllabus.ts:9](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/gantt/models/syllabus.ts#L9)

## Type Declaration

### color?

> `optional` **color?**: `null` \| `string`

Default colour id (custom colour or Hive subject); unset ⇒ none.

### courseIds?

> `optional` **courseIds?**: [`CourseId`](../../../../course/type-aliases/CourseId.md)[]

Courses (מסלולים) this syllabus belongs to.

### description?

> `optional` **description?**: `string`

Free text describing the syllabus, edited in the syllabus dialog.

### hiveIds

> **hiveIds**: `number`[]

### leadInstructorIds?

> `optional` **leadInstructorIds?**: `number`[]

Hive ids of the אחראי מקצוע instructors.

### modules

> **modules**: [`GanttModuleId`](../../shared/type-aliases/GanttModuleId.md)[]

### shuffleDescriptions?

> `optional` **shuffleDescriptions?**: [`ShuffleDescriptions`](../../../../../gantt/shuffle-names/type-aliases/ShuffleDescriptions.md)

Shuffle name → description. A shuffle is a Hive student group, and this
mirrors that group's staff-only description (max 100 chars).

### shuffleHiveGroups?

> `optional` **shuffleHiveGroups?**: [`ShuffleHiveGroups`](../../../../../gantt/shuffle-names/type-aliases/ShuffleHiveGroups.md)

Shuffle name → explicitly linked Hive student-group id (#774). A shuffle
without an entry matches the Hive group with its exact name.

### shuffles?

> `optional` **shuffles?**: `string`[]

Student group ("shuffle") names for this syllabus (e.g. "ניצה", "לחם").
Empty/undefined ⇒ the syllabus has a single, unnamed group.

### title

> **title**: `string`
