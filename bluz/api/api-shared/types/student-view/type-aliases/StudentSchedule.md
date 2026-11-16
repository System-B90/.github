[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentSchedule

# Type Alias: StudentSchedule

> **StudentSchedule** = `Omit`\<[`ApiStudentScheduleGetResponse`](ApiStudentScheduleGetResponse.md), `"courseGroups"` \| `"courseNames"` \| `"courseOptions"` \| `"events"` \| `"ownCourses"` \| `"roomNames"`\> & `object`

Defined in: [ui/src/api-shared/types/student-view.ts:111](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-shared/types/student-view.ts#L111)

Client-side result of `apiGetStudentSchedule`, names resolved.

## Type Declaration

### courseOptions

> **courseOptions**: `string`[]

### events

> **events**: [`StudentEvent`](StudentEvent.md)[]

### ownCourses

> **ownCourses**: `string`[]
