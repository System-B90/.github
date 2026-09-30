[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentSchedule

# Type Alias: StudentSchedule

> **StudentSchedule** = `Omit`\<[`ApiStudentScheduleGetResponse`](ApiStudentScheduleGetResponse.md), `"courseGroups"` \| `"courseNames"` \| `"events"` \| `"roomNames"`\> & `object`

Defined in: [ui/src/api-shared/types/student-view.ts:86](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/student-view.ts#L86)

Client-side result of `apiGetStudentSchedule`, names resolved.

## Type Declaration

### events

> **events**: [`StudentEvent`](StudentEvent.md)[]
