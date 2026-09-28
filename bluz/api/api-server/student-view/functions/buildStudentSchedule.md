[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-view](../index.md) / buildStudentSchedule

# Function: buildStudentSchedule()

> **buildStudentSchedule**(`date`, `controller`): `Promise`\<[`ApiStudentScheduleGetResponse`](../../../api-shared/types/student-view/type-aliases/ApiStudentScheduleGetResponse.md)\>

Defined in: [ui/src/api-server/student-view.ts:185](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-server/student-view.ts#L185)

Builds the student projection of a single day's schedule.

Two exclusions are enforced in the Mongo query itself rather than in the
mapper below, so no future refactor of the mapping can leak them: hidden
events (`hidden: true`) and anything outside the requested day. Archived
events are excluded by `DbEvent.getInRange` itself.

## Parameters

### date

`string`

### controller

[`DatabaseController`](../../mongo-db-controller/classes/DatabaseController.md)

## Returns

`Promise`\<[`ApiStudentScheduleGetResponse`](../../../api-shared/types/student-view/type-aliases/ApiStudentScheduleGetResponse.md)\>
