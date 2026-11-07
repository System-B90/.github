[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/GanttContentCommands](../index.md) / GanttContentCommands

# Function: GanttContentCommands()

> **GanttContentCommands**(): `null`

Defined in: [ui/src/components/app-commands/GanttContentCommands.tsx:86](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/app-commands/GanttContentCommands.tsx#L86)

Contributes the loaded curriculum's syllabuses, modules and events to the
entity lane, reusing the same flattened item list and scroll-into-view
navigation as the gantt view's own inline search.

Renders nothing — mount it inside `CurriculumView`, where both the curriculum
state and the search-nav context are available.

## Returns

`null`
