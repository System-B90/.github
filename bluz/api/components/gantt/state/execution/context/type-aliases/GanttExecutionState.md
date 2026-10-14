[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/execution/context](../index.md) / GanttExecutionState

# Type Alias: GanttExecutionState

> **GanttExecutionState** = `object`

Defined in: [ui/src/components/gantt/state/execution/context.ts:6](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/state/execution/context.ts#L6)

## Properties

### events

> **events**: `Record`\<[`GanttEventId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md), [`GanttEventExecution`](../../../../../../api-shared/types/gantt/execution/type-aliases/GanttEventExecution.md)\>

Defined in: [ui/src/components/gantt/state/execution/context.ts:8](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/state/execution/context.ts#L8)

Keyed by gantt event id; empty ⇒ curriculum not cut (or still loading).

***

### hasLoaded

> **hasLoaded**: `boolean`

Defined in: [ui/src/components/gantt/state/execution/context.ts:11](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/state/execution/context.ts#L11)

True once at least one fetch completed (distinguishes "not cut" from "loading").

***

### isLoading

> **isLoading**: `boolean`

Defined in: [ui/src/components/gantt/state/execution/context.ts:9](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/state/execution/context.ts#L9)
