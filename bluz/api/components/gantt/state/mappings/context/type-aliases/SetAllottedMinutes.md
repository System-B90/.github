[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/mappings/context](../index.md) / SetAllottedMinutes

# Type Alias: SetAllottedMinutes

> **SetAllottedMinutes** = (`{
    moduleId,
    eventId,
    dayId,
    allottedMinutes,
}`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/gantt/state/mappings/context.ts:47](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/state/mappings/context.ts#L47)

Sets the minutes an event is allotted on one of its mapped days.

## Parameters

### \{
    moduleId,
    eventId,
    dayId,
    allottedMinutes,
\}

#### allottedMinutes

`number`

#### dayId

[`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)

#### eventId

[`GanttEventId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md)

#### moduleId

[`GanttModuleId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttModuleId.md)

## Returns

`Promise`\<`boolean`\>
