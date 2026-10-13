[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / EventDaySpan

# Type Alias: EventDaySpan

> **EventDaySpan** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:216](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L216)

## Properties

### dayIds

> **dayIds**: [`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:218](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L218)

Day ids the event occupies, starting at its mapped day.

***

### minutesPerDay

> **minutesPerDay**: `number`[]

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:220](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L220)

Minutes consumed on each spanned day (parallel to `dayIds`).

***

### multiDay?

> `optional` **multiDay?**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:227](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L227)

True when the event is mapped onto several days, each with its own
allotted minutes: `dayIds` are then its mapped days, not a contiguous run.

***

### spillover

> **spillover**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:222](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L222)

True when the event overflows its start day onto subsequent day(s).
