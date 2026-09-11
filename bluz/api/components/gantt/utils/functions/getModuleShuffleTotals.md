[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / getModuleShuffleTotals

# Function: getModuleShuffleTotals()

> **getModuleShuffleTotals**(`module`, `fieldName`, `state`, `occurrenceCtx?`): `Record`\<`string`, `number`\> \| `null`

Defined in: [ui/src/components/gantt/utils.tsx:115](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/utils.tsx#L115)

Per-shuffle sums of an event field for a module, or null when none of the
module's events are shuffle-tagged (⇒ all shuffles are identical).

## Parameters

### module

[`GanttModule`](../../../../api-shared/types/gantt/models/module/type-aliases/GanttModule.md)

### fieldName

`NumberFieldKeys`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)\>

### state

[`NormalizedStore`](../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

### occurrenceCtx?

[`RecurrenceOccurrenceContext`](../type-aliases/RecurrenceOccurrenceContext.md)

## Returns

`Record`\<`string`, `number`\> \| `null`
