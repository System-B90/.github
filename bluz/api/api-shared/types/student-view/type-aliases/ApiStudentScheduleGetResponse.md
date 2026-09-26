[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / ApiStudentScheduleGetResponse

# Type Alias: ApiStudentScheduleGetResponse

> **ApiStudentScheduleGetResponse** = `object`

Defined in: [ui/src/api-shared/types/student-view.ts:66](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/student-view.ts#L66)

## Properties

### calendarDayEndTime

> **calendarDayEndTime**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:82](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/student-view.ts#L82)

***

### calendarDayStartTime

> **calendarDayStartTime**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:81](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/student-view.ts#L81)

The staff calendar's own grid bounds (`HH:mm`), so the student board
shows the same window instead of a bare 00:00-24:00 day. Carried on the
response because the student bundle mounts no settings provider.

***

### courseGroups

> **courseGroups**: `number`[][]

Defined in: [ui/src/api-shared/types/student-view.ts:73](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/student-view.ts#L73)

Distinct course-name index sets referenced by events.

***

### courseNames

> **courseNames**: `string`[]

Defined in: [ui/src/api-shared/types/student-view.ts:71](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/student-view.ts#L71)

Course / shuffle display names referenced by `courseGroups`.

***

### date

> **date**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:68](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/student-view.ts#L68)

The day the events belong to, `yyyy-MM-dd` in the app timezone.

***

### events

> **events**: [`StudentEventWire`](StudentEventWire.md)[]

Defined in: [ui/src/api-shared/types/student-view.ts:69](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/student-view.ts#L69)

***

### roomNames

> **roomNames**: `string`[]

Defined in: [ui/src/api-shared/types/student-view.ts:75](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/student-view.ts#L75)

Room display names referenced by `events[].rooms`.
