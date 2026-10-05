[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/student-schedule](../index.md) / resolveStudentSchedule

# Function: resolveStudentSchedule()

> **resolveStudentSchedule**(`__namedParameters`): [`StudentSchedule`](../../types/student-view/type-aliases/StudentSchedule.md)

Defined in: [ui/src/api-shared/student-schedule.ts:10](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/student-schedule.ts#L10)

Expands the normalized schedule response back into per-event names.
Groups resolve once, so events sharing a course set share one array.

## Parameters

### \_\_namedParameters

[`ApiStudentScheduleGetResponse`](../../types/student-view/type-aliases/ApiStudentScheduleGetResponse.md)

## Returns

[`StudentSchedule`](../../types/student-view/type-aliases/StudentSchedule.md)
