[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-fab/CurriculumActionItems](../index.md) / GanttCreationDeletionCallbackProps

# Type Alias: GanttCreationDeletionCallbackProps

> **GanttCreationDeletionCallbackProps** = `object`

Defined in: [ui/src/components/gantt/curriculum-fab/CurriculumActionItems.tsx:24](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-fab/CurriculumActionItems.tsx#L24)

## Properties

### onCreate?

> `optional` **onCreate?**: (`newCurriculum`) => `void`

Defined in: [ui/src/components/gantt/curriculum-fab/CurriculumActionItems.tsx:25](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-fab/CurriculumActionItems.tsx#L25)

#### Parameters

##### newCurriculum

[`GanttCurriculumDocument`](../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)

#### Returns

`void`

***

### onDelete?

> `optional` **onDelete?**: (`deletedCurriculumId`) => `void`

Defined in: [ui/src/components/gantt/curriculum-fab/CurriculumActionItems.tsx:26](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-fab/CurriculumActionItems.tsx#L26)

#### Parameters

##### deletedCurriculumId

[`GanttCurriculumId`](../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

#### Returns

`void`
