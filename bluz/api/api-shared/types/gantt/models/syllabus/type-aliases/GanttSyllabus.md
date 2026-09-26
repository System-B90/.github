[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/syllabus](../index.md) / GanttSyllabus

# Type Alias: GanttSyllabus

> **GanttSyllabus** = `object` & [`BaseGantItem`](../../shared/type-aliases/BaseGantItem.md)

Defined in: [ui/src/api-shared/types/gantt/models/syllabus.ts:6](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/models/syllabus.ts#L6)

## Type Declaration

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

### shuffles?

> `optional` **shuffles?**: `string`[]

Student group ("shuffle") names for this syllabus (e.g. "ניצה", "לחם").
Empty/undefined ⇒ the syllabus has a single, unnamed group.

### title

> **title**: `string`
