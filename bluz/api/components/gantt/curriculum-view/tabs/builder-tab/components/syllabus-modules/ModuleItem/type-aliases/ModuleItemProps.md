[**TypeDoc API**](../../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/builder-tab/components/syllabus-modules/ModuleItem](../index.md) / ModuleItemProps

# Type Alias: ModuleItemProps

> **ModuleItemProps** = `object` & `PaperProps`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/builder-tab/components/syllabus-modules/ModuleItem.tsx:23](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/tabs/builder-tab/components/syllabus-modules/ModuleItem.tsx#L23)

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
