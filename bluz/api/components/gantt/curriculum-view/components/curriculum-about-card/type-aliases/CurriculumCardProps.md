[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/curriculum-view/components/curriculum-about-card](../index.md) / CurriculumCardProps

# Type Alias: CurriculumCardProps

> **CurriculumCardProps** = `object` & `Omit`\<`CardProps`, `"sx"`\> & [`GanttCreationDeletionCallbackProps`](../../../../curriculum-fab/CurriculumActionItems/type-aliases/GanttCreationDeletionCallbackProps.md)

Defined in: [ui/src/components/gantt/curriculum-view/components/curriculum-about-card/index.tsx:15](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/components/curriculum-about-card/index.tsx#L15)

## Type Declaration

### curriculum

> **curriculum**: [`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md) \| `undefined`

### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md) \| `null`

### setCurrentCurriculum

> **setCurrentCurriculum**: `Dispatch`\<`SetStateAction`\<[`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md) \| `null`\>\>
