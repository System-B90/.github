[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/curriculum](../index.md) / GanttCurriculum

# Type Alias: GanttCurriculum

> **GanttCurriculum** = `object` & [`BaseGantItem`](../../shared/type-aliases/BaseGantItem.md)

Defined in: [ui/src/api-shared/types/gantt/models/curriculum.ts:5](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/models/curriculum.ts#L5)

## Type Declaration

### description

> **description**: `string`

### isArchived

> **isArchived**: `boolean`

Archived curriculums are kept as reference, grouped below drafts.

### isDraft

> **isDraft**: `boolean`

### startDate

> **startDate**: `null` \| `string`

### syllabuses

> **syllabuses**: [`GanttSyllabusId`](../../syllabus/type-aliases/GanttSyllabusId.md)[]

### title

> **title**: `string`

### weeks

> **weeks**: [`GanttWeekId`](../../week/type-aliases/GanttWeekId.md)[]
