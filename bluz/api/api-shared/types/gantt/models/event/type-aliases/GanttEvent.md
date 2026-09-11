[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/event](../index.md) / GanttEvent

# Type Alias: GanttEvent

> **GanttEvent** = `object` & [`BaseGantItem`](../../shared/type-aliases/BaseGantItem.md)

Defined in: [ui/src/api-shared/types/gantt/models/event.ts:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/models/event.ts#L25)

## Type Declaration

### allocatedDuration

> **allocatedDuration**: `number`

### comment

> **comment**: `null` \| `string`

### constraints

> **constraints**: [`GanttConstraint`](../../constraint/type-aliases/GanttConstraint.md)[]

### hiveLessonId

> **hiveLessonId**: `null` \| `number`

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

### systemRequirements

> **systemRequirements**: `string`[]

Free-text system requirements.

### title

> **title**: `string`

### type

> **type**: [`ModuleEventType`](../enumerations/ModuleEventType.md)
