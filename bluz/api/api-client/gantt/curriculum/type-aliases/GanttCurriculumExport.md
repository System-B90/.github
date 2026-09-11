[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/curriculum](../index.md) / GanttCurriculumExport

# Type Alias: GanttCurriculumExport

> **GanttCurriculumExport** = `object`

Defined in: [ui/src/api-client/gantt/curriculum.ts:23](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/curriculum.ts#L23)

Shape returned by `GET /api/gantt/curriculums/[id]/export` — the full
curriculum tree plus its day mappings and constraints, versioned so a
future export format change can be detected on import.

## Properties

### constraints

> **constraints**: [`GanttConstraint`](../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]

Defined in: [ui/src/api-client/gantt/curriculum.ts:27](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/curriculum.ts#L27)

***

### curriculum

> **curriculum**: [`RawBaseDocument`](../../../../api-shared/types/gantt/api-layer/type-aliases/RawBaseDocument.md)

Defined in: [ui/src/api-client/gantt/curriculum.ts:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/curriculum.ts#L25)

***

### mappings

> **mappings**: [`GanttCurriculumEventDayMapping`](../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)[]

Defined in: [ui/src/api-client/gantt/curriculum.ts:26](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/curriculum.ts#L26)

***

### version

> **version**: `string`

Defined in: [ui/src/api-client/gantt/curriculum.ts:24](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/curriculum.ts#L24)
