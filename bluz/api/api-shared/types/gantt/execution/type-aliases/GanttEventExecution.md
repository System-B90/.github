[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/execution](../index.md) / GanttEventExecution

# Type Alias: GanttEventExecution

> **GanttEventExecution** = `object`

Defined in: [ui/src/api-shared/types/gantt/execution.ts:47](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/execution.ts#L47)

## Properties

### drifted

> **drifted**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/execution.ts:58](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/execution.ts#L58)

True when any occurrence drifted.

***

### ganttEventId

> **ganttEventId**: [`GanttEventId`](../../models/event/type-aliases/GanttEventId.md)

Defined in: [ui/src/api-shared/types/gantt/execution.ts:48](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/execution.ts#L48)

***

### occurrences

> **occurrences**: [`OccurrenceExecution`](OccurrenceExecution.md)[]

Defined in: [ui/src/api-shared/types/gantt/execution.ts:49](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/execution.ts#L49)

***

### totals

> **totals**: `object`

Defined in: [ui/src/api-shared/types/gantt/execution.ts:51](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/execution.ts#L51)

Aggregates, mainly useful for recurring events.

#### actualMinutes

> **actualMinutes**: `number`

#### occurrencesActual

> **occurrencesActual**: `number`

#### occurrencesPlanned

> **occurrencesPlanned**: `number`

#### plannedMinutes

> **plannedMinutes**: `number`
