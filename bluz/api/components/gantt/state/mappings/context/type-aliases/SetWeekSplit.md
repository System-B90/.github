[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/mappings/context](../index.md) / SetWeekSplit

# Type Alias: SetWeekSplit

> **SetWeekSplit** = (`{
    moduleId,
    eventId,
    dayId,
    weekSplitMinutes,
}`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/state/mappings/context.ts:43](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/state/mappings/context.ts#L43)

Sets the minutes-per-week split of an event mapping (#768).

## Parameters

### \{
    moduleId,
    eventId,
    dayId,
    weekSplitMinutes,
\}

#### dayId

[`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)

#### eventId

[`GanttEventId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md)

#### moduleId

[`GanttModuleId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttModuleId.md)

#### weekSplitMinutes

`number`[]

## Returns

`Promise`\<`void`\>
