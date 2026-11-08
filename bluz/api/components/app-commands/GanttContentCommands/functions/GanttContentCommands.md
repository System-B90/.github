[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/GanttContentCommands](../index.md) / GanttContentCommands

# Function: GanttContentCommands()

> **GanttContentCommands**(): `null`

Defined in: [ui/src/components/app-commands/GanttContentCommands.tsx:86](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/app-commands/GanttContentCommands.tsx#L86)

Contributes the loaded curriculum's syllabuses, modules and events to the
entity lane, reusing the same flattened item list and scroll-into-view
navigation as the gantt view's own inline search.

Renders nothing — mount it inside `CurriculumView`, where both the curriculum
state and the search-nav context are available.

## Returns

`null`
