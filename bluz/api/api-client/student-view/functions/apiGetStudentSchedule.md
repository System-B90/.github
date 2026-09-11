[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/student-view](../index.md) / apiGetStudentSchedule

# Function: apiGetStudentSchedule()

> **apiGetStudentSchedule**(`date`, `props?`): `Promise`\<[`ApiStudentScheduleGetResponse`](../../../api-shared/types/student-view/type-aliases/ApiStudentScheduleGetResponse.md)\>

Defined in: [ui/src/api-client/student-view.ts:13](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/student-view.ts#L13)

Fetches the student projection of one day's schedule.

`date` is a *staff preview* affordance only — a student session that sends
it is rejected by the server, which always serves its own current day.

## Parameters

### date

`string` \| `undefined`

### props?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

## Returns

`Promise`\<[`ApiStudentScheduleGetResponse`](../../../api-shared/types/student-view/type-aliases/ApiStudentScheduleGetResponse.md)\>
