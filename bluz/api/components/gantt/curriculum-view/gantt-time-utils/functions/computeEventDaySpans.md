[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / computeEventDaySpans

# Function: computeEventDaySpans()

> **computeEventDaySpans**(`__namedParameters`): `Record`\<`string`, [`EventDaySpan`](../type-aliases/EventDaySpan.md)\>

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:288](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L288)

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
