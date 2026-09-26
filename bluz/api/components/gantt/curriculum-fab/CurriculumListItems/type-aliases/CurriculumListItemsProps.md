[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-fab/CurriculumListItems](../index.md) / CurriculumListItemsProps

# Type Alias: CurriculumListItemsProps

> **CurriculumListItemsProps** = `object` & [`GanttCreationDeletionCallbackProps`](../../CurriculumActionItems/type-aliases/GanttCreationDeletionCallbackProps.md)

Defined in: [ui/src/components/gantt/curriculum-fab/CurriculumListItems.tsx:15](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-fab/CurriculumListItems.tsx#L15)

## Type Declaration

### currentCurriculum?

> `optional` **currentCurriculum?**: [`GanttCurriculumId`](../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md) \| `null`

### curriculumsData

> **curriculumsData**: `Record`\<[`GanttCurriculumId`](../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md), [`GanttCurriculumDocument`](../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)\>

### groups

> **groups**: [`CurriculumGroups`](../../../state/curriculum-list/types/type-aliases/CurriculumGroups.md)

### isFetchingDetails

> **isFetchingDetails**: `boolean`

### setCurrentCurriculum

> **setCurrentCurriculum**: `Dispatch`\<`SetStateAction`\<[`GanttCurriculumId`](../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md) \| `null`\>\>
