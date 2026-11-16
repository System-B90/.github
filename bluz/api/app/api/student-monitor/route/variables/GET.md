[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/student-monitor/route](../index.md) / GET

# Variable: GET

> `const` **GET**: [`ServerApi`](../../../../../api-server/common/type-aliases/ServerApi.md)\<`void`, [`ApiStudentMonitorGetResponse`](../../../../../api-shared/types/student-monitor/type-aliases/ApiStudentMonitorGetResponse.md)\>

Defined in: [ui/src/app/api/student-monitor/route.ts:74](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/app/api/student-monitor/route.ts#L74)

GET /api/student-monitor?date=yyyy-MM-dd — staff-only: every student's
focused time on the board that day, with the suspected attempts recorded
against them (and against `anonymous`).

Deliberately outside `student-view/`: this is the tracking data *about*
students, which a student must never read. A Checker is refused too
(`CHECKER_DENIED_API_PREFIXES`).
