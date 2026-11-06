[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / Event

# Type Alias: Event

> **Event** = `object`

Defined in: [ui/src/api-shared/types/event.ts:36](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L36)

Represents a standard calendar event in the Bluz schedule.

## Properties

### color?

> `optional` **color?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:90](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L90)

***

### courses

> **courses**: [`CourseId`](../../course/type-aliases/CourseId.md)[]

Defined in: [ui/src/api-shared/types/event.ts:51](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L51)

***

### endTime

> **endTime**: `Dayjs`

Defined in: [ui/src/api-shared/types/event.ts:49](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L49)

***

### fake?

> `optional` **fake?**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:97](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L97)

"פיקטיבי" marker (issue #102): shown to students as a normal event but
acts as a placeholder for Checkers/Segel. Fake events are not wired to
a Hive subject/module/lesson — they carry only a manual color override
and a comment.

***

### ganttCurriculumId?

> `optional` **ganttCurriculumId?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:116](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L116)

Curriculum the event was cut from (עקרון "גזירה ללו"ז"). Lets the
schedule event dialog's "go to gantt" link resolve `?gc=` — without it
the gantt page has no curriculum to load and the link is a no-op.
Absent for normal events and for events cut before this field existed.

***

### ganttEventId?

> `optional` **ganttEventId?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:104](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L104)

Gantt event this schedule event was cut from (גזירה ללו"ז); absent for
normal events. Set by the curriculum cut endpoint (#118), or by hand in
the event dialog. A write sending "" for it (or its two siblings below)
clears it — see `GANTT_LINK_FIELDS` in `api-server/db-event.ts`.

***

### ganttOccurrenceDate?

> `optional` **ganttOccurrenceDate?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:109](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L109)

ISO date (yyyy-MM-dd) of the planned occurrence — disambiguates
recurrence occurrences of the same gantt event. Absent for normal events.

***

### hidden

> **hidden**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:58](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L58)

***

### hiveLesson?

> `optional` **hiveLesson?**: [`HiveLessonId`](../../hive/type-aliases/HiveLessonId.md) \| `null`

Defined in: [ui/src/api-shared/types/event.ts:47](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L47)

The Hive lesson a Segel picked. Hive's own rules on it decide which
queue each group gets; Bluz only assigns it to the event's groups when
the event goes live (#1025).

***

### hiveModule

> **hiveModule**: `null` \| `number`

Defined in: [ui/src/api-shared/types/event.ts:41](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L41)

Module ID; null once cleared (JSON drops undefined, so a clear must be null).

***

### id

> **id**: [`EventId`](EventId.md)

Defined in: [ui/src/api-shared/types/event.ts:37](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L37)

***

### instructors

> **instructors**: `number`[]

Defined in: [ui/src/api-shared/types/event.ts:53](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L53)

***

### lecturers?

> `optional` **lecturers?**: [`PersonId`](PersonId.md)[]

Defined in: [ui/src/api-shared/types/event.ts:54](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L54)

***

### locked

> **locked**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:57](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L57)

***

### name

> **name**: `string`

Defined in: [ui/src/api-shared/types/event.ts:38](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L38)

***

### notes

> **notes**: `string`

Defined in: [ui/src/api-shared/types/event.ts:56](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L56)

***

### parked?

> `optional` **parked?**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:72](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L72)

Taken off the grid into the unassigned-events box (#981): kept with its
times and duration, but not drawn, not shown to students and never sent
live to Hive until it is dropped back onto the schedule.

***

### personalTalk

> **personalTalk**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:60](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L60)

***

### required

> **required**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:59](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L59)

***

### restoredAfterDelete?

> `optional` **restoredAfterDelete?**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:78](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L78)

Set by a gantt reload when it re-creates an occurrence the user had
deleted from the schedule: the event comes back parked, and the box
marks it so the user knows why it reappeared.

***

### rooms

> **rooms**: [`ResolvableRoom`](../../room/type-aliases/ResolvableRoom.md)[]

Defined in: [ui/src/api-shared/types/event.ts:52](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L52)

***

### splitAcrossBreaks

> **splitAcrossBreaks**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:89](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L89)

When true, a break (הפסקה) the event runs into interrupts it instead of
overlapping it: the event pauses at the break's start and resumes when
it ends, as many times as needed.

This changes only how the event is *drawn*. `startTime` and `endTime`
always describe the net working span, so an event's duration can never
change as a side effect of a break being added, moved or removed — the
calendar simply re-lays it out. See `api-shared/break-windows.ts`.

***

### startTime

> **startTime**: `Dayjs`

Defined in: [ui/src/api-shared/types/event.ts:48](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L48)

***

### studentName?

> `optional` **studentName?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:66](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L66)

Name shown to students in /student-view instead of the auto-set one
(#966). Blank or absent means "use the auto-set name". Schedule-side
data: a gantt reload never touches it.

***

### subject

> **subject**: `number`

Defined in: [ui/src/api-shared/types/event.ts:39](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L39)

***

### tags

> **tags**: `number`[]

Defined in: [ui/src/api-shared/types/event.ts:55](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L55)

***

### type

> **type**: [`EventType`](../enumerations/EventType.md)

Defined in: [ui/src/api-shared/types/event.ts:50](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L50)

***

### updatedAt?

> `optional` **updatedAt?**: `number`

Defined in: [ui/src/api-shared/types/event.ts:130](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L130)

Client-stamped revision (epoch ms) set at save time (#156). Used as an
optimistic-concurrency guard: an incoming upsert (server resolve echo or
WS broadcast) is applied only when strictly newer than the copy already
in state, so a self-echo or a stale broadcast can never overwrite a newer
local edit. Absent on legacy events (treated as always-overwritable).

***

### weekTemplateId?

> `optional` **weekTemplateId?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:122](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/event.ts#L122)

Week template the event's week was cut with (#997). A reload, or saving
that template with "apply to cut weeks", re-plans the week with it.
Absent for normal events and for weeks cut before templates existed.
