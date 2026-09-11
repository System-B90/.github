[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-scheduling](../index.md) / useGanttScheduling

# Function: useGanttScheduling()

> **useGanttScheduling**(`__namedParameters`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-scheduling.ts:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-scheduling.ts#L16)

## Parameters

### \_\_namedParameters

#### curriculumMappings

`Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

#### dateOfDayId

(`dayId`) => `string` \| `undefined`

Calendar date of a day, for the recurrence window (#468).

#### eventMappings

`Record`\<`string`, `string`\>

#### linearDays

`string`[]

#### recurrenceExceptionState

[`GanttRecurrenceExceptionState`](../../../../../../state/recurrence-exceptions/types/type-aliases/GanttRecurrenceExceptionState.md)

#### state

[`NormalizedStore`](../../../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

## Returns

`object`

### eventSpans

> **eventSpans**: `Record`\<`string`, [`EventDaySpan`](../../../../../gantt-time-utils/type-aliases/EventDaySpan.md)\>

### scheduledMinutesByDay

> **scheduledMinutesByDay**: `Record`\<`string`, `number`\>
