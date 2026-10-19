[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCurriculumCutResponse

# Type Alias: ApiCurriculumCutResponse

> **ApiCurriculumCutResponse** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:108](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L108)

## Properties

### createdCourses

> **createdCourses**: `object`[]

Defined in: [ui/src/api-shared/types/gantt/cut.ts:114](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L114)

Courses that were newly created for shuffles during the cut.

#### id

> **id**: `string`

#### name

> **name**: `string`

***

### createdEvents

> **createdEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:110](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L110)

Number of schedule events created.

***

### hiveSubjectsUnavailable

> **hiveSubjectsUnavailable**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:137](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L137)

True when Hive could not be reached for the module → subject map during
this cut and events were written without their subject (and so without
their color) because of it (#662). The cut itself succeeded; running
"עדכון הלו״ז לפי הגאנט" once Hive is reachable repairs those events.

***

### insertedBreaks

> **insertedBreaks**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:130](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L130)

הפסקה events the break post-pass created.

***

### overlaps

> **overlaps**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:116](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L116)

Occurrences that overlap each other after stacking (informational).

***

### parkedEvents

> **parkedEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:128](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L128)

Events cut into the unassigned box (ארגז): week-only ones under
`parkWeekOnly`, and day overflow under the `park` resolution.

***

### replacedEvents?

> `optional` **replacedEvents?**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:112](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L112)

Earlier cut events of the week a single-week cut replaced (#970).

***

### spilledEvents

> **spilledEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:118](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L118)

Events the balancer moved to a later day in the same week.

***

### spills

> **spills**: [`CutSpillDetail`](../../../../gantt/cut-planner/type-aliases/CutSpillDetail.md)[]

Defined in: [ui/src/api-shared/types/gantt/cut.ts:123](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L123)

The same relocations, one entry each, so the dialog can expand the count
into exactly what moved and where.
