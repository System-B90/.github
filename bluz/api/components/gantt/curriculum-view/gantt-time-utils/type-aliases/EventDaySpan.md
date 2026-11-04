[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / EventDaySpan

# Type Alias: EventDaySpan

> **EventDaySpan** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:262](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L262)

## Properties

### dayIds

> **dayIds**: [`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:264](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L264)

Day ids the event occupies, starting at its mapped day.

***

### minutesPerDay

> **minutesPerDay**: `number`[]

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:266](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L266)

Minutes consumed on each spanned day (parallel to `dayIds`).

***

### multiDay?

> `optional` **multiDay?**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:273](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L273)

True when the event is mapped onto several days, each with its own
allotted minutes: `dayIds` are then its mapped days, not a contiguous run.

***

### spillover

> **spillover**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:268](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L268)

True when the event overflows its start day onto subsequent day(s).
