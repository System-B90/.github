[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / ApiStudentScheduleGetResponse

# Type Alias: ApiStudentScheduleGetResponse

> **ApiStudentScheduleGetResponse** = `object`

Defined in: [ui/src/api-shared/types/student-view.ts:69](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L69)

## Properties

### calendarDayEndTime

> **calendarDayEndTime**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:85](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L85)

***

### calendarDayStartTime

> **calendarDayStartTime**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:84](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L84)

The staff calendar's own grid bounds (`HH:mm`), so the student board
shows the same window instead of a bare 00:00-24:00 day. Carried on the
response because the student bundle mounts no settings provider.

***

### courseGroups

> **courseGroups**: `number`[][]

Defined in: [ui/src/api-shared/types/student-view.ts:76](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L76)

Distinct course-name index sets referenced by events.

***

### courseNames

> **courseNames**: `string`[]

Defined in: [ui/src/api-shared/types/student-view.ts:74](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L74)

Course / shuffle display names referenced by `courseGroups`.

***

### date

> **date**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:71](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L71)

The day the events belong to, `yyyy-MM-dd` in the app timezone.

***

### events

> **events**: [`StudentEventWire`](StudentEventWire.md)[]

Defined in: [ui/src/api-shared/types/student-view.ts:72](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L72)

***

### roomNames

> **roomNames**: `string`[]

Defined in: [ui/src/api-shared/types/student-view.ts:78](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L78)

Room display names referenced by `events[].rooms`.
