[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/execution/context](../index.md) / GanttExecutionContextType

# Type Alias: GanttExecutionContextType

> **GanttExecutionContextType** = `object`

Defined in: [ui/src/components/gantt/state/execution/context.ts:14](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/components/gantt/state/execution/context.ts#L14)

## Properties

### recreateOccurrence

> **recreateOccurrence**: (`ganttEventId`, `occurrenceDate`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/state/execution/context.ts:22](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/components/gantt/state/execution/context.ts#L22)

Re-creates the schedule event for one deleted occurrence (#682), then
refreshes the comparison so the new "actual" side shows up.

#### Parameters

##### ganttEventId

[`GanttEventId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md)

##### occurrenceDate

`string`

#### Returns

`Promise`\<`void`\>

***

### refreshExecution

> **refreshExecution**: () => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/state/execution/context.ts:17](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/components/gantt/state/execution/context.ts#L17)

Re-fetches the execution comparison from the server.

#### Returns

`Promise`\<`void`\>

***

### state

> **state**: [`GanttExecutionState`](GanttExecutionState.md)

Defined in: [ui/src/components/gantt/state/execution/context.ts:15](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/components/gantt/state/execution/context.ts#L15)
