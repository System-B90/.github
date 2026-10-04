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

Defined in: [ui/src/components/gantt/state/mappings/context.ts:23](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/state/mappings/context.ts#L23)

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
