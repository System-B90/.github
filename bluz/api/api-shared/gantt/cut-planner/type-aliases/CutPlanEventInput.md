[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanEventInput

# Type Alias: CutPlanEventInput

> **CutPlanEventInput** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:72](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L72)

## Properties

### allocatedDuration

> **allocatedDuration**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:78](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L78)

Per-curriculum allocated duration (minutes); falls back to `minimumDuration` when falsy.

***

### constraints?

> `optional` **constraints?**: [`GanttConstraint`](../../../types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:99](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L99)

Constraints owned by this event.

***

### groupId?

> `optional` **groupId?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:104](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L104)

Shuffle group (#699). Siblings mapped to the same day are the same lesson
for different shuffles, so they share one start time instead of stacking.

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:73](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L73)

***

### minimumDuration

> **minimumDuration**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:76](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L76)

***

### moduleId?

> `optional` **moduleId?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:93](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L93)

Owning gantt module — drives module cohesion during spillover.

***

### recurrence

> **recurrence**: [`EventRecurrence`](../../../types/gantt/models/event/enumerations/EventRecurrence.md)

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:75](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L75)

***

### recurrenceEndDate?

> `optional` **recurrenceEndDate?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:81](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L81)

***

### recurrenceStartDate?

> `optional` **recurrenceStartDate?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:80](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L80)

Recurrence window bounds ("YYYY-MM-DD"); null/absent ⇒ unbounded (#468).

***

### roomName?

> `optional` **roomName?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:97](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L97)

Assigned room name once the cut assigns rooms; null today.

***

### splitAcrossBreaks

> **splitAcrossBreaks**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:87](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L87)

When true, an overlapping meal/break window splits this event instead
of bumping it past the window: runs up to the window's start, resumes
after it ends (end time pushed out by the window's length).

***

### splitAcrossWeeks?

> `optional` **splitAcrossWeeks?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:89](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L89)

May run over consecutive weeks per its mapping's split (#768).

***

### syllabusId?

> `optional` **syllabusId?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:95](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L95)

Owning syllabus — drives the between-syllabuses break rule.

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:74](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L74)

***

### type?

> `optional` **type?**: [`ModuleEventType`](../../../types/gantt/models/event/enumerations/ModuleEventType.md)

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:91](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L91)

Drives the break rules (long ע"ע runs, post-lecture, prayer avoidance).
