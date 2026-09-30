[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / EventDaySpan

# Type Alias: EventDaySpan

> **EventDaySpan** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:248](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L248)

## Properties

### dayIds

> **dayIds**: [`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:250](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L250)

Day ids the event occupies, starting at its mapped day.

***

### minutesPerDay

> **minutesPerDay**: `number`[]

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:252](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L252)

Minutes consumed on each spanned day (parallel to `dayIds`).

***

### spillover

> **spillover**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:254](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L254)

True when the event overflows its start day onto subsequent day(s).

***

### weekSplit?

> `optional` **weekSplit?**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:259](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L259)

True when the event's hours are split over consecutive weeks (#768):
`dayIds` are then one day per week, not a contiguous run.
