[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-view](../index.md) / buildStudentSchedule

# Function: buildStudentSchedule()

> **buildStudentSchedule**(`date`, `controller`, `ownGroups?`): `Promise`\<[`ApiStudentScheduleGetResponse`](../../../api-shared/types/student-view/type-aliases/ApiStudentScheduleGetResponse.md)\>

Defined in: [ui/src/api-server/student-view.ts:229](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/student-view.ts#L229)

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

### ownGroups?

[`OwnHiveGroups`](../../student-own-groups/type-aliases/OwnHiveGroups.md) \| `Promise`\<[`OwnHiveGroups`](../../student-own-groups/type-aliases/OwnHiveGroups.md) \| `null`\> \| `null`

The viewer's own Hive groups (`getOwnHiveGroups`), or null
for staff and when Hive could not say. They only pick the board's default
selection (`ownCourses`); they never widen or narrow the events served.

## Returns

`Promise`\<[`ApiStudentScheduleGetResponse`](../../../api-shared/types/student-view/type-aliases/ApiStudentScheduleGetResponse.md)\>
