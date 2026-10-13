[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanInput

# Type Alias: CutPlanInput

> **CutPlanInput** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:122](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L122)

## Properties

### breakfastTime?

> `optional` **breakfastTime?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:140](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L140)

Preferred meal times (`"HH:mm"`), blocked out as breaks during stacking. Any subset may be omitted.

***

### days

> **days**: `Record`\<`string`, [`CutPlanDayInput`](CutPlanDayInput.md)\>

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:127](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L127)

All days referenced by `weeks`, keyed by id.

***

### dayStartTime

> **dayStartTime**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:133](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L133)

Day-start time for stacking, `"HH:mm"`.

***

### dinnerTime?

> `optional` **dinnerTime?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:142](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L142)

***

### eventIdsByModule?

> `optional` **eventIdsByModule?**: `Record`\<`string`, `string`[]\>

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:157](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L157)

Module id → the event ids it contains, for module-level constraints.

***

### events

> **events**: [`CutPlanEventInput`](CutPlanEventInput.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:128](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L128)

***

### lunchTime?

> `optional` **lunchTime?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:141](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L141)

***

### mappings

> **mappings**: [`CutPlanMappingInput`](CutPlanMappingInput.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:130](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L130)

Event-to-day mappings (`cMDA` rows with an `eventId`).

***

### moduleConstraints?

> `optional` **moduleConstraints?**: `object`[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:151](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L151)

Constraints owned by gantt modules, fanned out to their events.

#### constraints

> **constraints**: [`GanttConstraint`](../../../types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]

#### moduleId

> **moduleId**: `string`

#### title

> **title**: `string`

***

### prayerTimes?

> `optional` **prayerTimes?**: `object`[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:149](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L149)

Prayer windows (`"HH:mm"` starts) read from the schedule settings by the
server and handed in here — the pure planner has no way to reach Mongo.
Soft windows: breaks prefer to cover them, lectures prefer to avoid them,
and neither ever extends a day. See `PRAYER_RULES`.

#### durationMinutes?

> `optional` **durationMinutes?**: `number`

#### name

> **name**: `string`

#### time

> **time**: `string`

***

### recurrenceExceptions

> **recurrenceExceptions**: [`CutPlanRecurrenceExceptionInput`](CutPlanRecurrenceExceptionInput.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:131](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L131)

***

### startDate

> **startDate**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:123](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L123)

***

### weekendHomeStartTime?

> `optional` **weekendHomeStartTime?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:138](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L138)

Sunday start time (`"HH:mm"`) when the trainee was home (not on
weekend duty). Falls back to `dayStartTime` when omitted.

***

### weeks

> **weeks**: [`CutPlanWeekInput`](CutPlanWeekInput.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:125](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L125)

Weeks in timeline (junction) order.
