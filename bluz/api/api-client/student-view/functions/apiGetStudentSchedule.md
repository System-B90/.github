[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/student-view](../index.md) / apiGetStudentSchedule

# Function: apiGetStudentSchedule()

> **apiGetStudentSchedule**(`date`, `props?`): `Promise`\<[`StudentSchedule`](../../../api-shared/types/student-view/type-aliases/StudentSchedule.md)\>

Defined in: [ui/src/api-client/student-view.ts:15](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-client/student-view.ts#L15)

Fetches the student projection of one day's schedule.

`date` is a *staff preview* affordance only — a student session that sends
it is rejected by the server, which always serves its own current day.

## Parameters

### date

`string` \| `undefined`

### props?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

## Returns

`Promise`\<[`StudentSchedule`](../../../api-shared/types/student-view/type-aliases/StudentSchedule.md)\>
