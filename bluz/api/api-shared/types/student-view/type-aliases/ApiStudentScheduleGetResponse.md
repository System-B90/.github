[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / ApiStudentScheduleGetResponse

# Type Alias: ApiStudentScheduleGetResponse

> **ApiStudentScheduleGetResponse** = `object`

Defined in: [ui/src/api-shared/types/student-view.ts:69](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/student-view.ts#L69)

## Properties

### calendarDayEndTime

> **calendarDayEndTime**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:91](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/student-view.ts#L91)

***

### calendarDayStartTime

> **calendarDayStartTime**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:90](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/student-view.ts#L90)

The staff calendar's own grid bounds (`HH:mm`), so the student board
shows the same window instead of a bare 00:00-24:00 day. Carried on the
response because the student bundle mounts no settings provider.

***

### courseGroups

> **courseGroups**: `number`[][]

Defined in: [ui/src/api-shared/types/student-view.ts:76](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/student-view.ts#L76)

Distinct course-name index sets referenced by events.

***

### courseNames

> **courseNames**: `string`[]

Defined in: [ui/src/api-shared/types/student-view.ts:74](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/student-view.ts#L74)

Course / shuffle display names referenced by `courseGroups`.

***

### courseOptions

> **courseOptions**: `number`[]

Defined in: [ui/src/api-shared/types/student-view.ts:82](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/student-view.ts#L82)

The board's filter options, indexing `courseNames` (#1027): courses the
day's events name plus their parents, and only the shuffles an event
names outright. Never a name `courseNames` would not carry anyway.

***

### date

> **date**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:71](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/student-view.ts#L71)

The day the events belong to, `yyyy-MM-dd` in the app timezone.

***

### events

> **events**: [`StudentEventWire`](StudentEventWire.md)[]

Defined in: [ui/src/api-shared/types/student-view.ts:72](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/student-view.ts#L72)

***

### roomNames

> **roomNames**: `string`[]

Defined in: [ui/src/api-shared/types/student-view.ts:84](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/student-view.ts#L84)

Room display names referenced by `events[].rooms`.
