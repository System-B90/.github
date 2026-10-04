[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/GanttGridView](../index.md) / GanttGridView

# Variable: GanttGridView

> `const` **GanttGridView**: `React.FC`\<[`GanttViewProps`](../../types/type-aliases/GanttViewProps.md)\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/GanttGridView.tsx:97](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/GanttGridView.tsx#L97)

Spreadsheet-style gantt: weeks as columns, events as rows, each cell the
hours the event takes that week (recurrence echoes and week splits
included). Syllabus/module summary rows sum their children and collapse.
Arrow keys move the selected cell; Shift+arrows/click select a range,
Ctrl+click adds or removes a cell. Enter opens the row's dialog; Space
toggles a summary row; + expands and - collapses it. An event's week cells are editable (type, Enter, F2 or
double-click; Delete clears): the value is allotted to that week on blur.
