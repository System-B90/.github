[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / ApiStudentScheduleGetResponse

# Type Alias: ApiStudentScheduleGetResponse

> **ApiStudentScheduleGetResponse** = `object`

Defined in: [ui/src/api-shared/types/student-view.ts:69](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L69)

## Properties

### calendarDayEndTime

> **calendarDayEndTime**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:101](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L101)

***

### calendarDayStartTime

> **calendarDayStartTime**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:100](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L100)

The staff calendar's own grid bounds (`HH:mm`), so the student board
shows the same window instead of a bare 00:00-24:00 day. Carried on the
response because the student bundle mounts no settings provider.

***

### courseGroups

> **courseGroups**: `number`[][]

Defined in: [ui/src/api-shared/types/student-view.ts:76](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L76)

Distinct course-name index sets referenced by events.

***

### courseNames

> **courseNames**: `string`[]

Defined in: [ui/src/api-shared/types/student-view.ts:74](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L74)

Course / shuffle display names referenced by `courseGroups`.

***

### courseOptions

> **courseOptions**: `number`[]

Defined in: [ui/src/api-shared/types/student-view.ts:82](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L82)

The board's filter options, indexing `courseNames` (#1027): courses the
day's events name plus their parents, and only the shuffles an event
names outright. Never a name `courseNames` would not carry anyway.

***

### date

> **date**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:71](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L71)

The day the events belong to, `yyyy-MM-dd` in the app timezone.

***

### events

> **events**: [`StudentEventWire`](StudentEventWire.md)[]

Defined in: [ui/src/api-shared/types/student-view.ts:72](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L72)

***

### ownCourses

> **ownCourses**: `number`[]

Defined in: [ui/src/api-shared/types/student-view.ts:92](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L92)

The viewer's own shuffles, indexing `courseNames`: the board's default
selection. Resolved server-side from the student's own Hive group
membership (their own token, never the service account). A subset of
both `courseNames` and `courseOptions`, so it names nothing the response
would not carry anyway. Empty for staff, when Hive is unreachable, and
when none of the student's shuffles has an event today — the board then
defaults to every event.

***

### refreshSeconds

> **refreshSeconds**: `number`

Defined in: [ui/src/api-shared/types/student-view.ts:107](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L107)

How often the board refetches, in seconds (staff-set, else the
deployment default; `0` = off). On every response so a change reaches
open boards at their next refetch.

***

### roomNames

> **roomNames**: `string`[]

Defined in: [ui/src/api-shared/types/student-view.ts:94](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/student-view.ts#L94)

Room display names referenced by `events[].rooms`.
