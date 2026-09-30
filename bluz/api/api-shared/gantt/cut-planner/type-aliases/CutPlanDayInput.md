[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanDayInput

# Type Alias: CutPlanDayInput

> **CutPlanDayInput** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:51](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L51)

Pure "cut" planner (#117): expands a curriculum's gantt data into dated,
timed schedule-event occurrences. No DB access, no I/O — the caller adapts
its own data (Drizzle rows, normalized store, etc.) into `CutPlanInput`.

## Properties

### dayEndTime?

> `optional` **dayEndTime?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:61](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L61)

Explicit end of this day's working window (`"HH:mm"`). Null/absent ⇒
derived as the day's start time plus `totalWorkingMinutes`, which is how
days behaved before the field existed.

***

### dayIndex

> **dayIndex**: [`GanttDayIndex`](../../../types/gantt/models/day/enumerations/GanttDayIndex.md)

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:53](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L53)

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:52](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L52)

***

### totalWorkingMinutes?

> `optional` **totalWorkingMinutes?**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:55](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L55)

Configured working minutes for this day; the fallback for a null end time.
