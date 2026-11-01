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

Defined in: [ui/src/components/gantt/state/mappings/context.ts:51](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/gantt/state/mappings/context.ts#L51)

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
