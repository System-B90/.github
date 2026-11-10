[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / recurrenceRootDayId

# Function: recurrenceRootDayId()

> **recurrenceRootDayId**(`eventId`, `mappings`, `linearDays`): `string` \| `undefined`

Defined in: [ui/src/components/gantt/utils.tsx:64](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/utils.tsx#L64)

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
