[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / computeEventDaySpans

# Function: computeEventDaySpans()

> **computeEventDaySpans**(`__namedParameters`): `Record`\<`string`, [`EventDaySpan`](../type-aliases/EventDaySpan.md)\>

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:250](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L250)

Computes, per mapped event, the days it actually occupies. An event whose
required minutes exceed its start day's working capacity dynamically
overflows the excess onto subsequent days. The database still stores only
the start-day mapping — this is a pure frontend layout computation.

## Parameters

### \_\_namedParameters

#### linearDays

`string`[]

#### mappings

`Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

#### state

[`NormalizedStore`](../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

## Returns

`Record`\<`string`, [`EventDaySpan`](../type-aliases/EventDaySpan.md)\>
