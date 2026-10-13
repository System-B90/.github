[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCurriculumCutResponse

# Type Alias: ApiCurriculumCutResponse

> **ApiCurriculumCutResponse** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:86](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L86)

## Properties

### createdCourses

> **createdCourses**: `object`[]

Defined in: [ui/src/api-shared/types/gantt/cut.ts:92](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L92)

Courses that were newly created for shuffles during the cut.

#### id

> **id**: `string`

#### name

> **name**: `string`

***

### createdEvents

> **createdEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:88](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L88)

Number of schedule events created.

***

### hiveSubjectsUnavailable

> **hiveSubjectsUnavailable**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:110](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L110)

True when Hive could not be reached for the module → subject map during
this cut and events were written without their subject (and so without
their colour) because of it (#662). The cut itself succeeded; running
"עדכון הלו״ז לפי הגאנט" once Hive is reachable repairs those events.

***

### insertedBreaks

> **insertedBreaks**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:103](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L103)

הפסקה events the break post-pass created.

***

### overlaps

> **overlaps**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:94](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L94)

Occurrences that overlap each other after stacking (informational).

***

### replacedEvents?

> `optional` **replacedEvents?**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:90](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L90)

Earlier cut events of the week a single-week cut replaced (#970).

***

### spilledEvents

> **spilledEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:96](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L96)

Events the balancer moved to a later day in the same week.

***

### spills

> **spills**: [`CutSpillDetail`](../../../../gantt/cut-planner/type-aliases/CutSpillDetail.md)[]

Defined in: [ui/src/api-shared/types/gantt/cut.ts:101](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L101)

The same relocations, one entry each, so the dialog can expand the count
into exactly what moved and where.
