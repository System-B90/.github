[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanInput

# Type Alias: CutPlanInput

> **CutPlanInput** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:123](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L123)

## Properties

### breakfastTime?

> `optional` **breakfastTime?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:141](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L141)

Preferred meal times (`"HH:mm"`), blocked out as breaks during stacking. Any subset may be omitted.

***

### days

> **days**: `Record`\<`string`, [`CutPlanDayInput`](CutPlanDayInput.md)\>

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:128](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L128)

All days referenced by `weeks`, keyed by id.

***

### dayStartTime

> **dayStartTime**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:134](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L134)

Day-start time for stacking, `"HH:mm"`.

***

### dinnerTime?

> `optional` **dinnerTime?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:143](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L143)

***

### eventIdsByModule?

> `optional` **eventIdsByModule?**: `Record`\<`string`, `string`[]\>

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:158](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L158)

Module id → the event ids it contains, for module-level constraints.

***

### events

> **events**: [`CutPlanEventInput`](CutPlanEventInput.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:129](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L129)

***

### lunchTime?

> `optional` **lunchTime?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:142](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L142)

***

### mappings

> **mappings**: [`CutPlanMappingInput`](CutPlanMappingInput.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:131](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L131)

Event-to-day mappings (`cMDA` rows with an `eventId`).

***

### moduleConstraints?

> `optional` **moduleConstraints?**: `object`[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:152](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L152)

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

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:150](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L150)

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

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:132](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L132)

***

### startDate

> **startDate**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:124](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L124)

***

### weekendHomeStartTime?

> `optional` **weekendHomeStartTime?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:139](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L139)

Sunday start time (`"HH:mm"`) when the trainee was home (not on
weekend duty). Falls back to `dayStartTime` when omitted.

***

### weeks

> **weeks**: [`CutPlanWeekInput`](CutPlanWeekInput.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:126](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L126)

Weeks in timeline (junction) order.
