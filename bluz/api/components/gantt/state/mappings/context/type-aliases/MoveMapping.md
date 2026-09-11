[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/mappings/context](../index.md) / MoveMapping

# Type Alias: MoveMapping

> **MoveMapping** = (`{
    moduleId,
    eventId,
    from,
    to,
}`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/state/mappings/context.ts:21](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/mappings/context.ts#L21)

## Parameters

### \{
    moduleId,
    eventId,
    from,
    to,
\}

#### eventId

[`GanttEventId`](../../../../../../api-shared/types/gantt/models/event/type-aliases/GanttEventId.md) \| `null`

#### from

\{ `d`: [`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md); \}

#### from.d

[`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)

#### moduleId

[`GanttModuleId`](../../../../../../api-shared/types/gantt/models/module/type-aliases/GanttModuleId.md)

#### to

\{ `d`: [`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md); \}

#### to.d

[`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)

## Returns

`Promise`\<`void`\>
