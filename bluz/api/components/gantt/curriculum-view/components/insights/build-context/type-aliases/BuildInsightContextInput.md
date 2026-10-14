[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/insights/build-context](../index.md) / BuildInsightContextInput

# Type Alias: BuildInsightContextInput

> **BuildInsightContextInput** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:25](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L25)

## Properties

### constraintsByEvent

> **constraintsByEvent**: `Record`\<`string`, [`GanttConstraint`](../../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]\>

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:31](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L31)

Constraints binding each event (own + modules').

***

### curriculum

> **curriculum**: [`GanttCurriculumDocument`](../../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:26](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L26)

***

### exceptions

> **exceptions**: `Record`\<`string`, [`GanttEventRecurrenceException`](../../../../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)\>

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:29](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L29)

***

### execution

> **execution**: [`InsightContext`](../../types/type-aliases/InsightContext.md)\[`"execution"`\]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:35](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L35)

***

### instructorName

> **instructorName**: [`InsightContext`](../../types/type-aliases/InsightContext.md)\[`"instructorName"`\]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:33](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L33)

***

### mappings

> **mappings**: `Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:28](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L28)

***

### now

> **now**: `Dayjs`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:32](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L32)

***

### outsiderName

> **outsiderName**: [`InsightContext`](../../types/type-aliases/InsightContext.md)\[`"outsiderName"`\]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:34](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L34)

***

### schedule

> **schedule**: `Pick`\<[`CurriculumStudentSchedule`](../../../../use-student-schedule/type-aliases/CurriculumStudentSchedule.md), `"byDay"` \| `"requiredMinutes"` \| `"spans"`\>

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:37](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L37)

One student's schedule — see `useCurriculumStudentSchedule`.

***

### state

> **state**: [`NormalizedStore`](../../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/build-context.ts:27](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/components/insights/build-context.ts#L27)
