[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentSchedule

# Type Alias: StudentSchedule

> **StudentSchedule** = `Omit`\<[`ApiStudentScheduleGetResponse`](ApiStudentScheduleGetResponse.md), `"courseGroups"` \| `"courseNames"` \| `"events"` \| `"roomNames"`\> & `object`

Defined in: [ui/src/api-shared/types/student-view.ts:86](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/student-view.ts#L86)

Client-side result of `apiGetStudentSchedule`, names resolved.

## Type Declaration

### events

> **events**: [`StudentEvent`](StudentEvent.md)[]
