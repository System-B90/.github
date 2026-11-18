[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / DayHeadroom

# Type Alias: DayHeadroom

> **DayHeadroom** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:277](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L277)

Per-day load tracker fed by each event placement.

## Properties

### consume

> **consume**: (`dayId`, `eventId`, `minutes`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:279](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L279)

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
