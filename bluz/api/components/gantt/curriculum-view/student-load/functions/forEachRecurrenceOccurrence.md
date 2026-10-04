[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / forEachRecurrenceOccurrence

# Function: forEachRecurrenceOccurrence()

> **forEachRecurrenceOccurrence**(`__namedParameters`, `visit`): `void`

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:363](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/student-load.ts#L363)

Calls `visit` once per recurrence echo of every mapped recurring event (its
start day excluded), with its root mapping's allotted minutes. Skipped and materialized
occurrences are left out.

## Parameters

### \_\_namedParameters

#### dateOf?

(`dayId`) => `string` \| `undefined`

#### exceptions

`Record`\<`string`, [`GanttEventRecurrenceException`](../../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)\>

#### linearDays

`string`[]

#### mappings

`Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

#### state

[`NormalizedStore`](../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

### visit

(`dayId`, `eventId`, `minutes`) => `void`

## Returns

`void`
