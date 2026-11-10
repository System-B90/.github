[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentSchedule

# Type Alias: StudentSchedule

> **StudentSchedule** = `Omit`\<[`ApiStudentScheduleGetResponse`](ApiStudentScheduleGetResponse.md), `"courseGroups"` \| `"courseNames"` \| `"courseOptions"` \| `"events"` \| `"ownCourses"` \| `"roomNames"`\> & `object`

Defined in: [ui/src/api-shared/types/student-view.ts:111](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L111)

Client-side result of `apiGetStudentSchedule`, names resolved.

## Type Declaration

### courseOptions

> **courseOptions**: `string`[]

### events

> **events**: [`StudentEvent`](StudentEvent.md)[]

### ownCourses

> **ownCourses**: `string`[]
