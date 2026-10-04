[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/event](../index.md) / GanttEvent

# Type Alias: GanttEvent

> **GanttEvent** = `object` & [`BaseGantItem`](../../shared/type-aliases/BaseGantItem.md)

Defined in: [ui/src/api-shared/types/gantt/models/event.ts:29](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/gantt/models/event.ts#L29)

## Type Declaration

### comment

> **comment**: `null` \| `string`

### constraints

> **constraints**: [`GanttConstraint`](../../constraint/type-aliases/GanttConstraint.md)[]

### courseIds?

> `optional` **courseIds?**: [`CourseId`](../../../../course/type-aliases/CourseId.md)[]

Courses (a subset of the syllabus' courses and their sub-courses) this
event is limited to. Non-empty ⇒ only students of those courses attend,
and shuffles are irrelevant: `shuffles` is empty and `groupId` null.
Empty/undefined ⇒ the event is for the whole syllabus.

### groupId

> **groupId**: `null` \| `string`

Shuffle group this event belongs to, or null when it stands alone.

The same lesson given to different shuffles, in parallel inside the
syllabus' shared block (same start and end for every shuffle), is stored
as one event per shuffle - separate rows, so each can be placed, cut and
linked to Hive independently - tied together by a shared `groupId`. The
group is what lets the UI show them as one row and lets time totals count
the longest member once instead of summing every member (#699).

### hiveLessonId

> **hiveLessonId**: [`HiveLessonId`](../../../../hive/type-aliases/HiveLessonId.md) \| `null`

Hive lesson id; null when unlinked.

### hiveModuleId

> **hiveModuleId**: `null` \| `number`

Hive module id; null when unlinked.

### hiveSubjectId

> **hiveSubjectId**: `null` \| `number`

Hive subject id; null when unlinked.

### isCritical

> **isCritical**: `boolean`

Marked קריטי.

### isPaWindow

> **isPaWindow**: `boolean`

Marked חלון פ"א.

### minimumDuration

> **minimumDuration**: `number`

### orchestratorId

> **orchestratorId**: `null` \| `number`

Hive id of the responsible instructor ("אחראי"); null when unassigned.

### recommendedLecturerIds

> **recommendedLecturerIds**: `string`[]

Outsider IDs, ordered by recommendation priority (top = most recommended).

### recurrence

> **recurrence**: [`EventRecurrence`](../enumerations/EventRecurrence.md)

### recurrenceEndDate

> **recurrenceEndDate**: `null` \| `string`

Last date the recurrence may echo onto ("YYYY-MM-DD"), or null for "to the
end of the timeline" (#468).

### recurrenceStartDate

> **recurrenceStartDate**: `null` \| `string`

First date the recurrence may echo onto ("YYYY-MM-DD"), or null for "from
wherever the event is mapped". Lets a recurring event start mid-course
instead of being pinned to the first week (#468).

### roomRequirement

> **roomRequirement**: [`RoomRequirement`](../enumerations/RoomRequirement.md)

### shuffles?

> `optional` **shuffles?**: `string`[]

Shuffle names (from the parent syllabus) this event applies to.
Empty/undefined ⇒ applies to all shuffles.

### splitAcrossBreaks

> **splitAcrossBreaks**: `boolean`

When true and this event overlaps a meal/break window during cutting,
it's split around the break instead of bumped past it: runs up to the
break's start, then resumes after it ends.

### splitAcrossWeeks

> **splitAcrossWeeks**: `boolean`

When true the event's hours may be split over consecutive weeks, as
defined per curriculum on its mapping in the timeline view (#768).

### systemRequirements

> **systemRequirements**: `string`[]

Free-text system requirements.

### title

> **title**: `string`

### type

> **type**: [`ModuleEventType`](../enumerations/ModuleEventType.md)
