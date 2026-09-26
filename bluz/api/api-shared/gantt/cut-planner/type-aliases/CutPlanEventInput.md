[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanEventInput

# Type Alias: CutPlanEventInput

> **CutPlanEventInput** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:71](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L71)

## Properties

### allocatedDuration

> **allocatedDuration**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:77](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L77)

Per-curriculum allocated duration (minutes); falls back to `minimumDuration` when falsy.

***

### constraints?

> `optional` **constraints?**: [`GanttConstraint`](../../../types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:96](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L96)

Constraints owned by this event.

***

### groupId?

> `optional` **groupId?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:101](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L101)

Shuffle group (#699). Siblings mapped to the same day are the same lesson
for different shuffles, so they share one start time instead of stacking.

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:72](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L72)

***

### minimumDuration

> **minimumDuration**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:75](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L75)

***

### moduleId?

> `optional` **moduleId?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:90](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L90)

Owning gantt module — drives module cohesion during spillover.

***

### recurrence

> **recurrence**: [`EventRecurrence`](../../../types/gantt/models/event/enumerations/EventRecurrence.md)

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:74](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L74)

***

### recurrenceEndDate?

> `optional` **recurrenceEndDate?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:80](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L80)

***

### recurrenceStartDate?

> `optional` **recurrenceStartDate?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:79](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L79)

Recurrence window bounds ("YYYY-MM-DD"); null/absent ⇒ unbounded (#468).

***

### roomName?

> `optional` **roomName?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:94](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L94)

Assigned room name once the cut assigns rooms; null today.

***

### splitAcrossBreaks

> **splitAcrossBreaks**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:86](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L86)

When true, an overlapping meal/break window splits this event instead
of bumping it past the window: runs up to the window's start, resumes
after it ends (end time pushed out by the window's length).

***

### syllabusId?

> `optional` **syllabusId?**: `null` \| `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:92](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L92)

Owning syllabus — drives the between-syllabuses break rule.

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:73](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L73)

***

### type?

> `optional` **type?**: [`ModuleEventType`](../../../types/gantt/models/event/enumerations/ModuleEventType.md)

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:88](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L88)

Drives the break rules (long ע"ע runs, post-lecture, prayer avoidance).
