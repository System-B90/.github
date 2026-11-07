[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/context](../index.md) / GanttCellContextType

# Type Alias: GanttCellContextType

> **GanttCellContextType** = `Pick`\<[`GanttContextType`](../../types/type-aliases/GanttContextType.md), `"dayCellWidth"` \| `"getDropWarning"`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/context.ts:24](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/context.ts#L24)

The two timeline values a day cell reads, apart from the rest. The full
context changes on every mapping change, and a cell reading it re-rendered
with every one of the (thousands of) cells on each drop. `getDropWarning`
here keeps one identity and calls the latest rules, so this value changes
only when the cell width does.
