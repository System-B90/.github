[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-rows](../index.md) / buildGridRows

# Function: buildGridRows()

> **buildGridRows**(`syllabusIds`, `placement`, `isSyllabusExpanded`, `isModuleExpanded`, `paths?`): [`GridRow`](../type-aliases/GridRow.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-rows.ts:115](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-rows.ts#L115)

The grid's visible rows in display order. A summary row sums all of its
children, collapsed or not. An event's required time is its duration times
its required occurrences. A syllabus with several shuffles gets one section
per shuffle ("Title (Shuffle)") holding only that shuffle's modules and
events; the syllabus row then shows the busiest shuffle, since students sit
in exactly one shuffle.

## Parameters

### syllabusIds

`string`[]

### placement

[`GridPlacement`](../type-aliases/GridPlacement.md)

### isSyllabusExpanded

(`key`) => `boolean`

### isModuleExpanded

(`key`) => `boolean`

### paths?

[`StudentPath`](../../../../../student-load/type-aliases/StudentPath.md)[] = `[]`

Course columns, one per leaf course; none ⇒ no presence computed.

## Returns

[`GridRow`](../type-aliases/GridRow.md)[]
