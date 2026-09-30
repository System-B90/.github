[**TypeDoc API**](../../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/builder-tab/components/syllabus-modules/ModuleItem](../index.md) / ModuleItemProps

# Type Alias: ModuleItemProps

> **ModuleItemProps** = `object` & `PaperProps`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/builder-tab/components/syllabus-modules/ModuleItem.tsx:23](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/curriculum-view/tabs/builder-tab/components/syllabus-modules/ModuleItem.tsx#L23)

Properties for the [ModuleItem](../functions/ModuleItem.md) component.

## Type Declaration

### dayId?

> `optional` **dayId?**: [`GanttDayId`](../../../../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)

Optional identifier of the day if the item is placed inside a week panel.

### moduleId

> **moduleId**: [`GanttModuleId`](../../../../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttModuleId.md)

The unique identifier of the Gantt module.

### syllabusId?

> `optional` **syllabusId?**: [`GanttSyllabusId`](../../../../../../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabusId.md)

Optional identifier of the syllabus if the item is in the sidebar.
