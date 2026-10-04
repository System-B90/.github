[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / RecurrenceOccurrenceContext

# Type Alias: RecurrenceOccurrenceContext

> **RecurrenceOccurrenceContext** = `object`

Defined in: [ui/src/components/gantt/utils.tsx:37](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/utils.tsx#L37)

Placement/exception data needed to count how many times a recurring event
actually occurs on the timeline. Omitted ⇒ every event counts once,
matching the pre-recurrence-aware behavior (e.g. before placement exists).

## Properties

### dateOf?

> `optional` **dateOf?**: (`dayId`) => `string` \| `undefined`

Defined in: [ui/src/components/gantt/utils.tsx:46](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/utils.tsx#L46)

Calendar date of a day ("YYYY-MM-DD"), so the recurrence window applies (#468).

#### Parameters

##### dayId

`string`

#### Returns

`string` \| `undefined`

***

### exceptions

> **exceptions**: `Record`\<`string`, [`GanttEventRecurrenceException`](../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)\>

Defined in: [ui/src/components/gantt/utils.tsx:40](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/utils.tsx#L40)

***

### linearDays

> **linearDays**: `string`[]

Defined in: [ui/src/components/gantt/utils.tsx:42](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/utils.tsx#L42)

Timeline day ids in chronological order.

***

### mappings

> **mappings**: `Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

Defined in: [ui/src/components/gantt/utils.tsx:39](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/utils.tsx#L39)

***

### onlyDayIds?

> `optional` **onlyDayIds?**: `ReadonlySet`\<`string`\>

Defined in: [ui/src/components/gantt/utils.tsx:44](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/utils.tsx#L44)

Count only occurrences on these days (e.g. one week); unplaced events count 0.
