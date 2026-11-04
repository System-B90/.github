[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/curriculum-list/types](../index.md) / groupCurriculumsByStatus

# Function: groupCurriculumsByStatus()

> **groupCurriculumsByStatus**(`curriculums`): [`CurriculumGroups`](../type-aliases/CurriculumGroups.md)

Defined in: [ui/src/components/gantt/state/curriculum-list/types.ts:50](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/gantt/state/curriculum-list/types.ts#L50)

Split curriculums into three buckets — active, drafts, archived — each sorted
by `updatedAt` descending. Render order is active → drafts → archived.

## Parameters

### curriculums

`Record`\<[`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md), [`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)\>

## Returns

[`CurriculumGroups`](../type-aliases/CurriculumGroups.md)
