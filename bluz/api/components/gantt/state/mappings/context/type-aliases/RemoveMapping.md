[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/mappings/context](../index.md) / RemoveMapping

# Type Alias: RemoveMapping

> **RemoveMapping** = (`{
    moduleId,
    eventId,
    dayId,
}`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/gantt/state/mappings/context.ts:40](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/gantt/state/mappings/context.ts#L40)

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
