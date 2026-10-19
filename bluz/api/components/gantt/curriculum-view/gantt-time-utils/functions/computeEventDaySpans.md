[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / computeEventDaySpans

# Function: computeEventDaySpans()

> **computeEventDaySpans**(`__namedParameters`): `Record`\<`string`, [`EventDaySpan`](../type-aliases/EventDaySpan.md)\>

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:256](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L256)

Computes, per mapped event, the days it occupies: one per mapping, in
timeline order, each taking that mapping's allotted minutes. Events never
overflow onto later days here — an over-full day shows as over capacity;
spreading hours is the cut's job. With `load`, each placement is recorded.

## Parameters

### \_\_namedParameters

#### linearDays

`string`[]

#### load?

[`DayHeadroom`](../type-aliases/DayHeadroom.md)

#### mappings

`Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

#### state

[`NormalizedStore`](../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

## Returns

`Record`\<`string`, [`EventDaySpan`](../type-aliases/EventDaySpan.md)\>
