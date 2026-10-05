[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentSchedule

# Type Alias: StudentSchedule

> **StudentSchedule** = `Omit`\<[`ApiStudentScheduleGetResponse`](ApiStudentScheduleGetResponse.md), `"courseGroups"` \| `"courseNames"` \| `"events"` \| `"roomNames"`\> & `object`

Defined in: [ui/src/api-shared/types/student-view.ts:86](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/student-view.ts#L86)

Client-side result of `apiGetStudentSchedule`, names resolved.

## Type Declaration

### events

> **events**: [`StudentEvent`](StudentEvent.md)[]
