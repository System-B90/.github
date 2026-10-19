[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / RecurrenceOccurrenceContext

# Type Alias: RecurrenceOccurrenceContext

> **RecurrenceOccurrenceContext** = `object`

Defined in: [ui/src/components/gantt/utils.tsx:38](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/utils.tsx#L38)

Placement/exception data needed to count how many times a recurring event
actually occurs on the timeline. Omitted ⇒ every event counts once,
matching the pre-recurrence-aware behavior (e.g. before placement exists).

## Properties

### constraintsByEvent

> **constraintsByEvent**: `Record`\<`string`, [`GanttConstraint`](../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]\>

Defined in: [ui/src/components/gantt/utils.tsx:49](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/utils.tsx#L49)

Constraints binding each event (own + modules'); echoes skip forbidden weekdays.

***

### dateOf?

> `optional` **dateOf?**: (`dayId`) => `string` \| `undefined`

Defined in: [ui/src/components/gantt/utils.tsx:47](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/utils.tsx#L47)

Calendar date of a day ("YYYY-MM-DD"), so the recurrence window applies (#468).

#### Parameters

##### dayId

`string`

#### Returns

`string` \| `undefined`

***

### exceptions

> **exceptions**: `Record`\<`string`, [`GanttEventRecurrenceException`](../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)\>

Defined in: [ui/src/components/gantt/utils.tsx:41](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/utils.tsx#L41)

***

### linearDays

> **linearDays**: `string`[]

Defined in: [ui/src/components/gantt/utils.tsx:43](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/utils.tsx#L43)

Timeline day ids in chronological order.

***

### mappings

> **mappings**: `Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

Defined in: [ui/src/components/gantt/utils.tsx:40](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/utils.tsx#L40)

***

### onlyDayIds?

> `optional` **onlyDayIds?**: `ReadonlySet`\<`string`\>

Defined in: [ui/src/components/gantt/utils.tsx:45](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/utils.tsx#L45)

Count only occurrences on these days (e.g. one week); unplaced events count 0.
