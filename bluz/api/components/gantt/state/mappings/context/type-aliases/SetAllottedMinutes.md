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

Defined in: [ui/src/components/gantt/state/mappings/context.ts:51](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/state/mappings/context.ts#L51)

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
