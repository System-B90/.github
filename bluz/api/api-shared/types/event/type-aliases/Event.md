[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / Event

# Type Alias: Event

> **Event** = `object`

Defined in: [ui/src/api-shared/types/event.ts:35](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L35)

Represents a standard calendar event in the Bluz schedule.

## Properties

### color?

> `optional` **color?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:76](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L76)

***

### courses

> **courses**: [`CourseId`](../../course/type-aliases/CourseId.md)[]

Defined in: [ui/src/api-shared/types/event.ts:55](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L55)

***

### endTime

> **endTime**: `Dayjs`

Defined in: [ui/src/api-shared/types/event.ts:53](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L53)

***

### fake?

> `optional` **fake?**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:83](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L83)

"פיקטיבי" marker (issue #102): shown to students as a normal event but
acts as a placeholder for Checkers/Segel. Fake events are not wired to
a Hive subject/module/lesson — they carry only a manual color override
and a comment.

***

### ganttCurriculumId?

> `optional` **ganttCurriculumId?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:100](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L100)

Curriculum the event was cut from (עקרון "גזירה ללו"ז"). Lets the
schedule event dialog's "go to gantt" link resolve `?cid=` — without it
the gantt page has no curriculum to load and the link is a no-op.
Absent for normal events and for events cut before this field existed.

***

### ganttEventId?

> `optional` **ganttEventId?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:88](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L88)

Gantt event this schedule event was cut from (גזירה ללו"ז); absent for
normal events. Set by the curriculum cut endpoint (#118).

***

### ganttOccurrenceDate?

> `optional` **ganttOccurrenceDate?**: `string`

Defined in: [ui/src/api-shared/types/event.ts:93](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L93)

ISO date (yyyy-MM-dd) of the planned occurrence — disambiguates
recurrence occurrences of the same gantt event. Absent for normal events.

***

### hidden

> **hidden**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:62](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L62)

***

### hiveLesson?

> `optional` **hiveLesson?**: `null` \| `number`

Defined in: [ui/src/api-shared/types/event.ts:40](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L40)

***

### hiveModule

> **hiveModule**: `number`

Defined in: [ui/src/api-shared/types/event.ts:39](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L39)

***

### hiveQueues?

> `optional` **hiveQueues?**: `Record`\<[`CourseId`](../../course/type-aliases/CourseId.md), `number`\>

Defined in: [ui/src/api-shared/types/event.ts:51](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L51)

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

Defined in: [ui/src/api-shared/types/event.ts:36](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L36)

***

### instructors

> **instructors**: `number`[]

Defined in: [ui/src/api-shared/types/event.ts:57](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L57)

***

### lecturers?

> `optional` **lecturers?**: [`PersonId`](PersonId.md)[]

Defined in: [ui/src/api-shared/types/event.ts:58](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L58)

***

### locked

> **locked**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:61](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L61)

***

### name

> **name**: `string`

Defined in: [ui/src/api-shared/types/event.ts:37](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L37)

***

### notes

> **notes**: `string`

Defined in: [ui/src/api-shared/types/event.ts:60](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L60)

***

### personalTalk

> **personalTalk**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:64](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L64)

***

### required

> **required**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:63](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L63)

***

### rooms

> **rooms**: [`ResolvableRoom`](../../room/type-aliases/ResolvableRoom.md)[]

Defined in: [ui/src/api-shared/types/event.ts:56](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L56)

***

### splitAcrossBreaks

> **splitAcrossBreaks**: `boolean`

Defined in: [ui/src/api-shared/types/event.ts:75](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L75)

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

Defined in: [ui/src/api-shared/types/event.ts:52](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L52)

***

### subject

> **subject**: `number`

Defined in: [ui/src/api-shared/types/event.ts:38](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L38)

***

### tags

> **tags**: `number`[]

Defined in: [ui/src/api-shared/types/event.ts:59](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L59)

***

### type

> **type**: [`EventType`](../enumerations/EventType.md)

Defined in: [ui/src/api-shared/types/event.ts:54](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L54)

***

### updatedAt?

> `optional` **updatedAt?**: `number`

Defined in: [ui/src/api-shared/types/event.ts:108](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L108)

Client-stamped revision (epoch ms) set at save time (#156). Used as an
optimistic-concurrency guard: an incoming upsert (server resolve echo or
WS broadcast) is applied only when strictly newer than the copy already
in state, so a self-echo or a stale broadcast can never overwrite a newer
local edit. Absent on legacy events (treated as always-overwritable).
