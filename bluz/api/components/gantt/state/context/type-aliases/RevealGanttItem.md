[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/state/context](../index.md) / RevealGanttItem

# Type Alias: RevealGanttItem

> **RevealGanttItem** = (`syllabusId`, `moduleId`, `eventId?`) => `void`

Defined in: [ui/src/components/gantt/state/context.ts:50](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/context.ts#L50)

Reveals a module/event row in the רצף זמן timeline: expands its ancestors,
scrolls it into view and flash-highlights it. The actual behavior is
registered by the Gantt view (`registerRevealHandler`); other flows (e.g.
event create/duplicate) trigger it via `requestReveal` (#325).

## Parameters

### syllabusId

[`GanttSyllabusId`](../../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabusId.md)

### moduleId

[`GanttModuleId`](../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttModuleId.md)

### eventId?

[`GanttEventId`](../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md)

## Returns

`void`
