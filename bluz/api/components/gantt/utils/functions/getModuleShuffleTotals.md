[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / getModuleShuffleTotals

# Function: getModuleShuffleTotals()

> **getModuleShuffleTotals**(`module`, `fieldName`, `state`, `occurrenceCtx?`): `Record`\<`string`, `number`\> \| `null`

Defined in: [ui/src/components/gantt/utils.tsx:161](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/utils.tsx#L161)

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
