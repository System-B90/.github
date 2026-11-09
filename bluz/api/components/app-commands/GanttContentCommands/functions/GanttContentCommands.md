[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/GanttContentCommands](../index.md) / GanttContentCommands

# Function: GanttContentCommands()

> **GanttContentCommands**(): `null`

Defined in: [ui/src/components/app-commands/GanttContentCommands.tsx:86](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/app-commands/GanttContentCommands.tsx#L86)

Contributes the loaded curriculum's syllabuses, modules and events to the
entity lane, reusing the same flattened item list and scroll-into-view
navigation as the gantt view's own inline search.

Renders nothing — mount it inside `CurriculumView`, where both the curriculum
state and the search-nav context are available.

## Returns

`null`
