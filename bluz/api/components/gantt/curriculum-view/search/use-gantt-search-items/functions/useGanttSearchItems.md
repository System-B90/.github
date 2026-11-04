[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/curriculum-view/search/use-gantt-search-items](../index.md) / useGanttSearchItems

# Function: useGanttSearchItems()

> **useGanttSearchItems**(): [`GanttSearchItem`](../type-aliases/GanttSearchItem.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/search/use-gantt-search-items.ts:35](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/gantt/curriculum-view/search/use-gantt-search-items.ts#L35)

Flatten the current curriculum into a hierarchically-ordered list of
searchable items (syllabus, then each of its modules, then each module's
events). Only the loaded curriculum is represented, so the search is
naturally scoped to the current curriculum.

## Returns

[`GanttSearchItem`](../type-aliases/GanttSearchItem.md)[]
