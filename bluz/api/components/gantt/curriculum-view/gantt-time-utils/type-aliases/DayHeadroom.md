[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / DayHeadroom

# Type Alias: DayHeadroom

> **DayHeadroom** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:228](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L228)

Per-day load tracker fed by each event placement.

## Properties

### consume

> **consume**: (`dayId`, `eventId`, `minutes`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:230](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L230)

Records that `eventId` uses `minutes` of `dayId`.

#### Parameters

##### dayId

[`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)

##### eventId

`string`

##### minutes

`number`

#### Returns

`void`
