[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentEvent

# Type Alias: StudentEvent

> **StudentEvent** = `object`

Defined in: [ui/src/api-shared/types/student-view.ts:25](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L25)

The *only* shape of a calendar event a student ("חניך") may ever receive
(#656). This is a security boundary, not a display preference: a student
session must never be able to obtain any other event field, from any
endpoint, by any parameter.

Deliberately absent, and why:
- `type`, `notes`, `tags`, `required`, `personalTalk`, `locked`,
  `splitAcrossBreaks` — staff-only attributes.
- `subject`, `hiveModule`, `hiveLesson`, `hiveQueues` — Hive identifiers.
  The event *color* is resolved to a hex string on the server precisely so
  the subject id behind it never crosses the wire.
- `instructors`, `lecturers` — staff//outsider identities.
- `gantt*` — curriculum provenance.
- `hidden`, `fake`, `archived` — hidden and archived events are dropped
  server-side and never represented here; fake events ("פיקטיבי", #102) are
  returned as ordinary events, indistinguishable by construction, because
  they are meant to look real to students.

Rooms and courses are carried as display names only — never as Hive class
ids or Bluz course ids.

## Properties

### color

> **color**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:36](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L36)

Fully resolved hex color (e.g. `#3f51b5`), never a color/subject id.

***

### courses

> **courses**: `string`[]

Defined in: [ui/src/api-shared/types/student-view.ts:40](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L40)

Course / shuffle display names.

***

### endTime

> **endTime**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:34](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L34)

***

### id

> **id**: [`EventId`](../../event/type-aliases/EventId.md)

Defined in: [ui/src/api-shared/types/student-view.ts:30](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L30)

The event's own UUID. Opaque. An event split across breaks arrives as
one entry per piece, all sharing this id.

***

### name

> **name**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:31](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L31)

***

### relatedCourses

> **relatedCourses**: `string`[]

Defined in: [ui/src/api-shared/types/student-view.ts:46](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L46)

`courses` plus every ancestor and descendant shuffle, as display names.
Filtering by a shuffle matches on this, so a child shuffle sees its
parents' events and a parent sees its children's.

***

### rooms

> **rooms**: `string`[]

Defined in: [ui/src/api-shared/types/student-view.ts:38](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L38)

Room display names.

***

### startTime

> **startTime**: `string`

Defined in: [ui/src/api-shared/types/student-view.ts:33](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/student-view.ts#L33)

ISO 8601 timestamps.
