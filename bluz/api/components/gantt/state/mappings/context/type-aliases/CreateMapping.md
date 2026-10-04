[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/mappings/context](../index.md) / CreateMapping

# Type Alias: CreateMapping

> **CreateMapping** = (`{
    moduleId,
    eventId,
    dayId,
}`) => `Promise`\<[`GanttCurriculumEventDayMapping`](../../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md) \| `undefined`\>

Defined in: [ui/src/components/gantt/state/mappings/context.ts:12](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/state/mappings/context.ts#L12)

## Parameters

### \{
    moduleId,
    eventId,
    dayId,
\}

#### allottedMinutes?

`number`

Omitted ⇒ the event's whole minimumDuration.

#### dayId

[`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)

#### eventId

[`GanttEventId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md) \| `null`

#### moduleId

[`GanttModuleId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttModuleId.md)

## Returns

`Promise`\<[`GanttCurriculumEventDayMapping`](../../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md) \| `undefined`\>
