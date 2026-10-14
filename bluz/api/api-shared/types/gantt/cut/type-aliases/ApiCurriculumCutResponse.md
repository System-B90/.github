[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCurriculumCutResponse

# Type Alias: ApiCurriculumCutResponse

> **ApiCurriculumCutResponse** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:91](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L91)

## Properties

### createdCourses

> **createdCourses**: `object`[]

Defined in: [ui/src/api-shared/types/gantt/cut.ts:97](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L97)

Courses that were newly created for shuffles during the cut.

#### id

> **id**: `string`

#### name

> **name**: `string`

***

### createdEvents

> **createdEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:93](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L93)

Number of schedule events created.

***

### hiveSubjectsUnavailable

> **hiveSubjectsUnavailable**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:115](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L115)

True when Hive could not be reached for the module → subject map during
this cut and events were written without their subject (and so without
their colour) because of it (#662). The cut itself succeeded; running
"עדכון הלו״ז לפי הגאנט" once Hive is reachable repairs those events.

***

### insertedBreaks

> **insertedBreaks**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:108](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L108)

הפסקה events the break post-pass created.

***

### overlaps

> **overlaps**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:99](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L99)

Occurrences that overlap each other after stacking (informational).

***

### replacedEvents?

> `optional` **replacedEvents?**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:95](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L95)

Earlier cut events of the week a single-week cut replaced (#970).

***

### spilledEvents

> **spilledEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:101](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L101)

Events the balancer moved to a later day in the same week.

***

### spills

> **spills**: [`CutSpillDetail`](../../../../gantt/cut-planner/type-aliases/CutSpillDetail.md)[]

Defined in: [ui/src/api-shared/types/gantt/cut.ts:106](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L106)

The same relocations, one entry each, so the dialog can expand the count
into exactly what moved and where.
