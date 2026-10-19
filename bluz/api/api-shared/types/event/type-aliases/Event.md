[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / Event

# Type Alias: Event

> **Event** = `object`

Defined in: [ui/src/api-shared/types/event.ts:36](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L36)

Represents a standard calendar event in the Bluz schedule.

## Properties

### color?

> `optional` **color?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:95](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L95)

***

### courses

> **courses**: [`CourseId`](../../course/type-aliases/CourseId.md)[]

Defined in: [ui/src/api-shared/types/event.ts:56](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L56)

***

### endTime

> **endTime**: `Dayjs`

Defined in: [ui/src/api-shared/types/event.ts:54](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L54)

***

### fake?

> `optional` **fake?**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:102](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L102)

"פיקטיבי" marker (issue #102): shown to students as a normal event but
acts as a placeholder for Checkers/Segel. Fake events are not wired to
a Hive subject/module/lesson — they carry only a manual color override
and a comment.

***

### ganttCurriculumId?

> `optional` **ganttCurriculumId?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:119](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L119)

Curriculum the event was cut from (עקרון "גזירה ללו"ז"). Lets the
schedule event dialog's "go to gantt" link resolve `?gc=` — without it
the gantt page has no curriculum to load and the link is a no-op.
Absent for normal events and for events cut before this field existed.

***

### ganttEventId?

> `optional` **ganttEventId?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:107](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L107)

Gantt event this schedule event was cut from (גזירה ללו"ז); absent for
normal events. Set by the curriculum cut endpoint (#118).

***

### ganttOccurrenceDate?

> `optional` **ganttOccurrenceDate?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:112](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L112)

ISO date (yyyy-MM-dd) of the planned occurrence — disambiguates
recurrence occurrences of the same gantt event. Absent for normal events.

***

### hidden

> **hidden**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:63](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L63)

***

### hiveLesson?

> `optional` **hiveLesson?**: [`HiveLessonId`](../../hive/type-aliases/HiveLessonId.md) \| `null`

Defined in: [ui/src/api-shared/types/event.ts:41](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L41)

***

### hiveModule

> **hiveModule**: `number`

Defined in: [ui/src/api-shared/types/event.ts:40](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L40)

***

### hiveQueues?

> `optional` **hiveQueues?**: `Record`\<[`CourseId`](../../course/type-aliases/CourseId.md), `number`\>

Defined in: [ui/src/api-shared/types/event.ts:52](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L52)

Per-shuffle Hive queue mapping: Bluz course id → Hive queue id. A course
is a shuffle, which is 1:1 with a Hive student group, so this is what
decides *which students* get *which queue* when the event goes live.

Setting it makes Bluz own a Hive lesson for this event: on every write
`api-server/hive/lesson-sync` reconciles a `Lesson` under `hiveModule`
plus one `LessonRule` per mapped shuffle, and stores the lesson id back
into `hiveLesson`. Clearing it (or archiving the event) deletes them.

***

### id

> **id**: [`EventId`](EventId.md)

Defined in: [ui/src/api-shared/types/event.ts:37](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L37)

***

### instructors

> **instructors**: `number`[]

Defined in: [ui/src/api-shared/types/event.ts:58](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L58)

***

### lecturers?

> `optional` **lecturers?**: [`PersonId`](PersonId.md)[]

Defined in: [ui/src/api-shared/types/event.ts:59](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L59)

***

### locked

> **locked**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:62](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L62)

***

### name

> **name**: `string`

Defined in: [ui/src/api-shared/types/event.ts:38](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L38)

***

### notes

> **notes**: `string`

Defined in: [ui/src/api-shared/types/event.ts:61](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L61)

***

### parked?

> `optional` **parked?**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:77](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L77)

Taken off the grid into the unassigned-events box (#981): kept with its
times and duration, but not drawn, not shown to students and never sent
live to Hive until it is dropped back onto the schedule.

***

### personalTalk

> **personalTalk**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:65](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L65)

***

### required

> **required**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:64](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L64)

***

### restoredAfterDelete?

> `optional` **restoredAfterDelete?**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:83](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L83)

Set by a gantt reload when it re-creates an occurrence the user had
deleted from the schedule: the event comes back parked, and the box
marks it so the user knows why it reappeared.

***

### rooms

> **rooms**: [`ResolvableRoom`](../../room/type-aliases/ResolvableRoom.md)[]

Defined in: [ui/src/api-shared/types/event.ts:57](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L57)

***

### splitAcrossBreaks

> **splitAcrossBreaks**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:94](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L94)

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

Defined in: [ui/src/api-shared/types/event.ts:53](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L53)

***

### studentName?

> `optional` **studentName?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:71](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L71)

Name shown to students in /student-view instead of the auto-set one
(#966). Blank or absent means "use the auto-set name". Schedule-side
data: a gantt reload never touches it.

***

### subject

> **subject**: `number`

Defined in: [ui/src/api-shared/types/event.ts:39](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L39)

***

### tags

> **tags**: `number`[]

Defined in: [ui/src/api-shared/types/event.ts:60](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L60)

***

### type

> **type**: [`EventType`](../enumerations/EventType.md)

Defined in: [ui/src/api-shared/types/event.ts:55](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L55)

***

### updatedAt?

> `optional` **updatedAt?**: `number`

Defined in: [ui/src/api-shared/types/event.ts:133](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L133)

Client-stamped revision (epoch ms) set at save time (#156). Used as an
optimistic-concurrency guard: an incoming upsert (server resolve echo or
WS broadcast) is applied only when strictly newer than the copy already
in state, so a self-echo or a stale broadcast can never overwrite a newer
local edit. Absent on legacy events (treated as always-overwritable).

***

### weekTemplateId?

> `optional` **weekTemplateId?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:125](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L125)

Week template the event's week was cut with (#997). A reload, or saving
that template with "apply to cut weeks", re-plans the week with it.
Absent for normal events and for weeks cut before templates existed.
