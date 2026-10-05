[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/insights/build-context](../index.md) / BuildInsightContextInput

# Type Alias: BuildInsightContextInput

> **BuildInsightContextInput** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:24](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L24)

## Properties

### curriculum

> **curriculum**: [`GanttCurriculumDocument`](../../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:25](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L25)

***

### exceptions

> **exceptions**: `Record`\<`string`, [`GanttEventRecurrenceException`](../../../../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)\>

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:28](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L28)

***

### execution

> **execution**: [`InsightContext`](../../types/type-aliases/InsightContext.md)\[`"execution"`\]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:32](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L32)

***

### instructorName

> **instructorName**: [`InsightContext`](../../types/type-aliases/InsightContext.md)\[`"instructorName"`\]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:30](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L30)

***

### mappings

> **mappings**: `Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:27](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L27)

***

### now

> **now**: `Dayjs`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:29](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L29)

***

### outsiderName

> **outsiderName**: [`InsightContext`](../../types/type-aliases/InsightContext.md)\[`"outsiderName"`\]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:31](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L31)

***

### schedule

> **schedule**: `Pick`\<[`CurriculumStudentSchedule`](../../../../use-student-schedule/type-aliases/CurriculumStudentSchedule.md), `"byDay"` \| `"requiredMinutes"` \| `"spans"`\>

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:34](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L34)

One student's schedule — see `useCurriculumStudentSchedule`.

***

### state

> **state**: [`NormalizedStore`](../../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:26](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L26)
