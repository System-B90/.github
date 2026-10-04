[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentSchedule

# Type Alias: StudentSchedule

> **StudentSchedule** = `Omit`\<[`ApiStudentScheduleGetResponse`](ApiStudentScheduleGetResponse.md), `"courseGroups"` \| `"courseNames"` \| `"events"` \| `"roomNames"`\> & `object`

Defined in: [ui/src/api-shared/types/student-view.ts:86](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/student-view.ts#L86)

Client-side result of `apiGetStudentSchedule`, names resolved.

## Type Declaration

### events

> **events**: [`StudentEvent`](StudentEvent.md)[]
