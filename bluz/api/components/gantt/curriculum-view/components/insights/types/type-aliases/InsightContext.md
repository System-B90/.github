[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/insights/types](../index.md) / InsightContext

# Type Alias: InsightContext

> **InsightContext** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:102](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L102)

Everything a generator needs, derived once per state change.

## Properties

### capacityMinutes

> **capacityMinutes**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:110](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L110)

***

### curriculum

> **curriculum**: [`GanttCurriculumDocument`](../../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:103](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L103)

***

### days

> **days**: [`InsightDay`](InsightDay.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:106](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L106)

***

### events

> **events**: [`InsightEvent`](InsightEvent.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:107](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L107)

***

### execution

> **execution**: `Record`\<`string`, [`GanttEventExecution`](../../../../../../../api-shared/types/gantt/execution/type-aliases/GanttEventExecution.md)\>

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:117](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L117)

תכנון מול ביצוע, keyed by gantt event id; empty ⇒ not cut yet.

***

### instructorName

> **instructorName**: (`id`) => `string`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:114](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L114)

#### Parameters

##### id

`number`

#### Returns

`string`

***

### now

> **now**: `Dayjs`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:113](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L113)

***

### outsiderName

> **outsiderName**: (`id`) => `string` \| `undefined`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:115](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L115)

#### Parameters

##### id

`string`

#### Returns

`string` \| `undefined`

***

### requiredMinutes

> **requiredMinutes**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:112](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L112)

***

### scheduledMinutes

> **scheduledMinutes**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:111](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L111)

***

### state

> **state**: [`NormalizedStore`](../../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:104](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L104)

***

### weeks

> **weeks**: [`InsightWeek`](InsightWeek.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:105](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L105)

***

### workEvents

> **workEvents**: [`InsightEvent`](InsightEvent.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/types.ts:109](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/components/insights/types.ts#L109)

Events outside the meal-breaks syllabus.
