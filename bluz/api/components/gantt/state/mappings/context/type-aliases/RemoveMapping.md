[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/mappings/context](../index.md) / RemoveMapping

# Type Alias: RemoveMapping

> **RemoveMapping** = (`{
    moduleId,
    eventId,
    dayId,
}`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/gantt/state/mappings/context.ts:40](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/state/mappings/context.ts#L40)

## Parameters

### \{
    moduleId,
    eventId,
    dayId,
\}

#### dayId

[`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)

#### eventId

[`GanttEventId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md) \| `null`

#### moduleId

[`GanttModuleId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttModuleId.md)

## Returns

`Promise`\<`boolean`\>
