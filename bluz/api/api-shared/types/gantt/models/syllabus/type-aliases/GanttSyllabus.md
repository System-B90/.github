[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/syllabus](../index.md) / GanttSyllabus

# Type Alias: GanttSyllabus

> **GanttSyllabus** = `object` & [`BaseGantItem`](../../shared/type-aliases/BaseGantItem.md)

Defined in: [ui/src/api-shared/types/gantt/models/syllabus.ts:10](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/models/syllabus.ts#L10)

## Type Declaration

### color?

> `optional` **color?**: `null` \| `string`

Default color id (custom color or Hive subject); unset ⇒ none.

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

### shortName?

> `optional` **shortName?**: `null` \| `string`

Short name / symbol prefixed to events cut from this syllabus (#973).
Unset ⇒ the linked Hive subject's symbol, else the title.

### shuffleDescriptions?

> `optional` **shuffleDescriptions?**: [`ShuffleDescriptions`](../../../../../gantt/shuffle-names/type-aliases/ShuffleDescriptions.md)

Shuffle name → description. A shuffle is a Hive student group, and this
mirrors that group's staff-only description (max 100 chars).

### shuffleHiveGroups?

> `optional` **shuffleHiveGroups?**: [`ShuffleHiveGroups`](../../../../../gantt/shuffle-names/type-aliases/ShuffleHiveGroups.md)

Shuffle name → explicitly linked Hive student-group id (#774). A shuffle
without an entry matches the Hive group with its exact name.

### shuffleLevels?

> `optional` **shuffleLevels?**: [`ShuffleLevels`](../../../../../gantt/shuffle-names/type-aliases/ShuffleLevels.md)

Shuffle name → staff (סגל) level (#991). The name itself is the
trainee (חניכים) name and never contains a level word.

### shuffles?

> `optional` **shuffles?**: `string`[]

Student group ("shuffle") names for this syllabus (e.g. "ניצה", "לחם").
Empty/undefined ⇒ the syllabus has a single, unnamed group.

### title

> **title**: `string`
