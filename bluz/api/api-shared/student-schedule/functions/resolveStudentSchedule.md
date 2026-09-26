[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/student-schedule](../index.md) / resolveStudentSchedule

# Function: resolveStudentSchedule()

> **resolveStudentSchedule**(`__namedParameters`): [`StudentSchedule`](../../types/student-view/type-aliases/StudentSchedule.md)

Defined in: [ui/src/api-shared/student-schedule.ts:10](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/student-schedule.ts#L10)

Expands the normalized schedule response back into per-event names.
Groups resolve once, so events sharing a course set share one array.

## Parameters

### \_\_namedParameters

[`ApiStudentScheduleGetResponse`](../../types/student-view/type-aliases/ApiStudentScheduleGetResponse.md)

## Returns

[`StudentSchedule`](../../types/student-view/type-aliases/StudentSchedule.md)
