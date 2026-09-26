[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/drizzle-normalize](../index.md) / NormalizedSyllabusSubtree

# Type Alias: NormalizedSyllabusSubtree

> **NormalizedSyllabusSubtree** = `object`

Defined in: [ui/src/api-client/gantt/drizzle-normalize.ts:52](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/gantt/drizzle-normalize.ts#L52)

Normalized store slices for a single syllabus and its module/event subtree.
Reused both by full-curriculum normalization and by the link flow (#320),
which receives one fully-populated `ApiSyllabus` and must fold its modules +
events into the store — not just the bare syllabus record.

## Properties

### events

> **events**: [`ModuleEventDocument`](../../module-event/type-aliases/ModuleEventDocument.md) & `object`[]

Defined in: [ui/src/api-client/gantt/drizzle-normalize.ts:55](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/gantt/drizzle-normalize.ts#L55)

***

### modules

> **modules**: [`ModuleDocument`](../../module/type-aliases/ModuleDocument.md) & `object`[]

Defined in: [ui/src/api-client/gantt/drizzle-normalize.ts:54](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/gantt/drizzle-normalize.ts#L54)

***

### syllabus

> **syllabus**: [`SyllabusDocument`](../../syllabus/type-aliases/SyllabusDocument.md) & `object`

Defined in: [ui/src/api-client/gantt/drizzle-normalize.ts:53](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/gantt/drizzle-normalize.ts#L53)

#### Type Declaration

##### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)
