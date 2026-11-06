[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / recurrenceRootDayId

# Function: recurrenceRootDayId()

> **recurrenceRootDayId**(`eventId`, `mappings`, `linearDays`): `string` \| `undefined`

Defined in: [ui/src/components/gantt/utils.tsx:64](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/components/gantt/utils.tsx#L64)

The day a recurrence echoes from: the event's earliest mapped day on the
timeline, as the cut and the student-load view root it. Map order is not
timeline order, so the first mapping found could be a later day.

## Parameters

### eventId

`string`

### mappings

`Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

### linearDays

`string`[]

## Returns

`string` \| `undefined`
