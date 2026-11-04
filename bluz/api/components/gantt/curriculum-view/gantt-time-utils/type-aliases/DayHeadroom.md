[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / DayHeadroom

# Type Alias: DayHeadroom

> **DayHeadroom** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:277](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L277)

Per-day load tracker fed by each event placement.

## Properties

### consume

> **consume**: (`dayId`, `eventId`, `minutes`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:279](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L279)

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
