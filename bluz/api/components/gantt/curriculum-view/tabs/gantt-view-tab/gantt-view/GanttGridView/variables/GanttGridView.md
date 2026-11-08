[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/GanttGridView](../index.md) / GanttGridView

# Variable: GanttGridView

> `const` **GanttGridView**: `React.FC`\<[`GanttViewProps`](../../types/type-aliases/GanttViewProps.md)\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/GanttGridView.tsx:113](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/GanttGridView.tsx#L113)

Spreadsheet-style gantt: weeks as columns, events as rows, each cell the
hours the event takes that week (recurrence echoes and week splits
included). Syllabus/module summary rows sum their children and collapse.
Arrow keys move the selected cell; Shift+arrows/click select a range,
Ctrl+click adds or removes a cell. Enter opens the row's dialog; Space
toggles a summary row; + expands and - collapses it. An event's week cells are editable (type, Enter, F2 or
double-click; Delete clears): the value is allotted to that week on blur.
