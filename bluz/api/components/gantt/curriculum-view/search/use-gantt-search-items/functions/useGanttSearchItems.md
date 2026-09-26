[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/curriculum-view/search/use-gantt-search-items](../index.md) / useGanttSearchItems

# Function: useGanttSearchItems()

> **useGanttSearchItems**(): [`GanttSearchItem`](../type-aliases/GanttSearchItem.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/search/use-gantt-search-items.ts:34](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/search/use-gantt-search-items.ts#L34)

Flatten the current curriculum into a hierarchically-ordered list of
searchable items (syllabus, then each of its modules, then each module's
events). Only the loaded curriculum is represented, so the search is
naturally scoped to the current curriculum.

## Returns

[`GanttSearchItem`](../type-aliases/GanttSearchItem.md)[]
