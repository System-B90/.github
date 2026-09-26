[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanInput

# Type Alias: CutPlanInput

> **CutPlanInput** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:115](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L115)

## Properties

### breakfastTime?

> `optional` **breakfastTime?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:133](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L133)

Preferred meal times (`"HH:mm"`), blocked out as breaks during stacking. Any subset may be omitted.

***

### days

> **days**: `Record`\<`string`, [`CutPlanDayInput`](CutPlanDayInput.md)\>

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:120](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L120)

All days referenced by `weeks`, keyed by id.

***

### dayStartTime

> **dayStartTime**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:126](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L126)

Day-start time for stacking, `"HH:mm"`.

***

### dinnerTime?

> `optional` **dinnerTime?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:135](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L135)

***

### eventIdsByModule?

> `optional` **eventIdsByModule?**: `Record`\<`string`, `string`[]\>

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:150](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L150)

Module id → the event ids it contains, for module-level constraints.

***

### events

> **events**: [`CutPlanEventInput`](CutPlanEventInput.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:121](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L121)

***

### lunchTime?

> `optional` **lunchTime?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:134](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L134)

***

### mappings

> **mappings**: [`CutPlanMappingInput`](CutPlanMappingInput.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:123](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L123)

Event-to-day mappings (`cMDA` rows with an `eventId`).

***

### moduleConstraints?

> `optional` **moduleConstraints?**: `object`[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:144](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L144)

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

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:142](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L142)

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

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:124](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L124)

***

### startDate

> **startDate**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:116](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L116)

***

### weekendHomeStartTime?

> `optional` **weekendHomeStartTime?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:131](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L131)

Sunday start time (`"HH:mm"`) when the trainee was home (not on
weekend duty). Falls back to `dayStartTime` when omitted.

***

### weeks

> **weeks**: [`CutPlanWeekInput`](CutPlanWeekInput.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:118](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L118)

Weeks in timeline (junction) order.
