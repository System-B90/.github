[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanDayInput

# Type Alias: CutPlanDayInput

> **CutPlanDayInput** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:49](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L49)

Pure "cut" planner (#117): expands a curriculum's gantt data into dated,
timed schedule-event occurrences. No DB access, no I/O — the caller adapts
its own data (Drizzle rows, normalized store, etc.) into `CutPlanInput`.

## Properties

### dayEndTime?

> `optional` **dayEndTime?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:59](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L59)

Explicit end of this day's working window (`"HH:mm"`). Null/absent ⇒
derived as the day's start time plus `totalWorkingMinutes`, which is how
days behaved before the field existed.

***

### dayIndex

> **dayIndex**: [`GanttDayIndex`](../../../types/gantt/models/day/enumerations/GanttDayIndex.md)

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:51](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L51)

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:50](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L50)

***

### totalWorkingMinutes?

> `optional` **totalWorkingMinutes?**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:53](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L53)

Configured working minutes for this day; the fallback for a null end time.
