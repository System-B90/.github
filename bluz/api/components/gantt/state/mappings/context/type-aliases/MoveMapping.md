[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/mappings/context](../index.md) / MoveMapping

# Type Alias: MoveMapping

> **MoveMapping** = (`{
    moduleId,
    eventId,
    from,
    to,
}`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/gantt/state/mappings/context.ts:23](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/state/mappings/context.ts#L23)

## Parameters

### \{
    moduleId,
    eventId,
    from,
    to,
\}

#### allottedMinutes?

`number`

Also re-allots the moved mapping.

#### eventId

[`GanttEventId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md) \| `null`

#### from

\{ `d`: [`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md); \}

#### from.d

[`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)

#### moduleId

[`GanttModuleId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttModuleId.md)

#### to

\{ `d`: [`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md); \}

#### to.d

[`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)

## Returns

`Promise`\<`boolean`\>
