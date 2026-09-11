[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanEventInput

# Type Alias: CutPlanEventInput

> **CutPlanEventInput** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:70](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L70)

## Properties

### allocatedDuration

> **allocatedDuration**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:76](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L76)

Per-curriculum allocated duration (minutes); falls back to `minimumDuration` when falsy.

***

### constraints?

> `optional` **constraints?**: [`GanttConstraint`](../../../types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:95](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L95)

Constraints owned by this event.

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:71](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L71)

***

### minimumDuration

> **minimumDuration**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:74](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L74)

***

### moduleId?

> `optional` **moduleId?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:89](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L89)

Owning gantt module — drives module cohesion during spillover.

***

### recurrence

> **recurrence**: [`EventRecurrence`](../../../types/gantt/models/event/enumerations/EventRecurrence.md)

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:73](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L73)

***

### recurrenceEndDate?

> `optional` **recurrenceEndDate?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:79](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L79)

***

### recurrenceStartDate?

> `optional` **recurrenceStartDate?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:78](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L78)

Recurrence window bounds ("YYYY-MM-DD"); null/absent ⇒ unbounded (#468).

***

### roomName?

> `optional` **roomName?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:93](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L93)

Assigned room name once the cut assigns rooms; null today.

***

### splitAcrossBreaks

> **splitAcrossBreaks**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:85](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L85)

When true, an overlapping meal/break window splits this event instead
of bumping it past the window: runs up to the window's start, resumes
after it ends (end time pushed out by the window's length).

***

### syllabusId?

> `optional` **syllabusId?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:91](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L91)

Owning syllabus — drives the between-syllabuses break rule.

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:72](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L72)

***

### type?

> `optional` **type?**: [`ModuleEventType`](../../../types/gantt/models/event/enumerations/ModuleEventType.md)

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:87](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L87)

Drives the break rules (long ע"ע runs, post-lecture, prayer avoidance).
