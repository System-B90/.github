[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/curriculum-list/types](../index.md) / groupCurriculumsByStatus

# Function: groupCurriculumsByStatus()

> **groupCurriculumsByStatus**(`curriculums`): [`CurriculumGroups`](../type-aliases/CurriculumGroups.md)

Defined in: [ui/src/components/gantt/state/curriculum-list/types.ts:48](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/curriculum-list/types.ts#L48)

Split curriculums into three buckets — active, drafts, archived — each sorted
by `updatedAt` descending. Render order is active → drafts → archived.

## Parameters

### curriculums

`Record`\<[`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md), [`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)\>

## Returns

[`CurriculumGroups`](../type-aliases/CurriculumGroups.md)
