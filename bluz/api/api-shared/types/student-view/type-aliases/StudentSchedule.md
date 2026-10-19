[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentSchedule

# Type Alias: StudentSchedule

> **StudentSchedule** = `Omit`\<[`ApiStudentScheduleGetResponse`](ApiStudentScheduleGetResponse.md), `"courseGroups"` \| `"courseNames"` \| `"events"` \| `"roomNames"`\> & `object`

Defined in: [ui/src/api-shared/types/student-view.ts:89](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L89)

Client-side result of `apiGetStudentSchedule`, names resolved.

## Type Declaration

### events

> **events**: [`StudentEvent`](StudentEvent.md)[]
