[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / DayHeadroom

# Type Alias: DayHeadroom

> **DayHeadroom** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:231](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L231)

Per-day load tracker fed by each event placement.

## Properties

### consume

> **consume**: (`dayId`, `eventId`, `minutes`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:233](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L233)

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
