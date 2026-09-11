[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/execution](../index.md) / OccurrenceExecution

# Type Alias: OccurrenceExecution

> **OccurrenceExecution** = `object`

Defined in: [ui/src/api-shared/types/gantt/execution.ts:33](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/execution.ts#L33)

## Properties

### actual

> **actual**: [`ActualOccurrenceExecution`](ActualOccurrenceExecution.md) \| `null`

Defined in: [ui/src/api-shared/types/gantt/execution.ts:42](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/execution.ts#L42)

null ⇒ the generated schedule event was deleted/archived.

***

### drifted

> **drifted**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/execution.ts:44](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/execution.ts#L44)

Convenience flag: actual missing or any compared field differs.

***

### occurrenceDate

> **occurrenceDate**: `string`

Defined in: [ui/src/api-shared/types/gantt/execution.ts:35](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/execution.ts#L35)

Planned occurrence date (yyyy-MM-dd) — the join key with the schedule.

***

### planned

> **planned**: `null` \| [`PlannedOccurrenceExecution`](PlannedOccurrenceExecution.md)

Defined in: [ui/src/api-shared/types/gantt/execution.ts:40](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/execution.ts#L40)

Planned attributes; null for orphaned actual events whose planned
occurrence no longer exists in the current plan (gantt edited post-cut).
