[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / recurrenceRootDayId

# Function: recurrenceRootDayId()

> **recurrenceRootDayId**(`eventId`, `mappings`, `linearDays`): `string` \| `undefined`

Defined in: [ui/src/components/gantt/utils.tsx:64](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/gantt/utils.tsx#L64)

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
