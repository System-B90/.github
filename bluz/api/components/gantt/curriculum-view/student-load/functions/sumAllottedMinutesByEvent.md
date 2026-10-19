[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / sumAllottedMinutesByEvent

# Function: sumAllottedMinutesByEvent()

> **sumAllottedMinutesByEvent**(`ctx`): `Map`\<`string`, `number`\>

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:426](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/gantt/curriculum-view/student-load.ts#L426)

Minutes each event is allotted in a curriculum: every one of its mappings'
allotted minutes, plus each surviving recurrence echo at its earliest
mapping's. The single read path for an event's scheduled time; 0 means
the event is documented but not part of the curriculum.

## Parameters

### ctx

#### constraintsByEvent

`Record`\<`string`, [`GanttConstraint`](../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]\>

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

## Returns

`Map`\<`string`, `number`\>
