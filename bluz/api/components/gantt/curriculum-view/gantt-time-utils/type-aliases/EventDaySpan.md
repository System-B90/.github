[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / EventDaySpan

# Type Alias: EventDaySpan

> **EventDaySpan** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:230](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L230)

## Properties

### dayIds

> **dayIds**: [`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:232](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L232)

Day ids the event occupies, starting at its mapped day.

***

### minutesPerDay

> **minutesPerDay**: `number`[]

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:234](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L234)

Minutes consumed on each spanned day (parallel to `dayIds`).

***

### multiDay?

> `optional` **multiDay?**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:241](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L241)

True when the event is mapped onto several days, each with its own
allotted minutes: `dayIds` are then its mapped days, not a contiguous run.

***

### spillover

> **spillover**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:236](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L236)

True when the event overflows its start day onto subsequent day(s).
