[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/insights/types](../index.md) / InsightContext

# Type Alias: InsightContext

> **InsightContext** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:104](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L104)

Everything a generator needs, derived once per state change.

## Properties

### capacityMinutes

> **capacityMinutes**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:112](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L112)

***

### curriculum

> **curriculum**: [`GanttCurriculumDocument`](../../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:105](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L105)

***

### days

> **days**: [`InsightDay`](InsightDay.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:108](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L108)

***

### events

> **events**: [`InsightEvent`](InsightEvent.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:109](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L109)

***

### execution

> **execution**: `Record`\<`string`, [`GanttEventExecution`](../../../../../../../api-shared/types/gantt/execution/type-aliases/GanttEventExecution.md)\>

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:119](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L119)

תכנון מול ביצוע, keyed by gantt event id; empty ⇒ not cut yet.

***

### instructorName

> **instructorName**: (`id`) => `string`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:116](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L116)

#### Parameters

##### id

`number`

#### Returns

`string`

***

### now

> **now**: `Dayjs`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:115](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L115)

***

### outsiderName

> **outsiderName**: (`id`) => `string` \| `undefined`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:117](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L117)

#### Parameters

##### id

`string`

#### Returns

`string` \| `undefined`

***

### requiredMinutes

> **requiredMinutes**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:114](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L114)

***

### scheduledMinutes

> **scheduledMinutes**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:113](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L113)

***

### state

> **state**: [`NormalizedStore`](../../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:106](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L106)

***

### weeks

> **weeks**: [`InsightWeek`](InsightWeek.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:107](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L107)

***

### workEvents

> **workEvents**: [`InsightEvent`](InsightEvent.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:111](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L111)

Events outside the meal-breaks syllabus.
