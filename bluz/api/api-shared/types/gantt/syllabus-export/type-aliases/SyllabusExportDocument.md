[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/syllabus-export](../index.md) / SyllabusExportDocument

# Type Alias: SyllabusExportDocument

> **SyllabusExportDocument** = `object`

Defined in: [ui/src/api-shared/types/gantt/syllabus-export.ts:7](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/gantt/syllabus-export.ts#L7)

What `GET /api/gantt/syllabuses/{id}/export` returns and the import accepts.

## Properties

### constraints

> **constraints**: `unknown`[]

Defined in: [ui/src/api-shared/types/gantt/syllabus-export.ts:13](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/gantt/syllabus-export.ts#L13)

***

### kind

> **kind**: *typeof* [`SYLLABUS_EXPORT_KIND`](../variables/SYLLABUS_EXPORT_KIND.md)

Defined in: [ui/src/api-shared/types/gantt/syllabus-export.ts:9](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/gantt/syllabus-export.ts#L9)

***

### sourceCurriculumId?

> `optional` **sourceCurriculumId?**: `string`

Defined in: [ui/src/api-shared/types/gantt/syllabus-export.ts:11](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/gantt/syllabus-export.ts#L11)

Curriculum whose allocated durations travel with the file.

***

### syllabus

> **syllabus**: [`ApiSyllabus`](../../api-layer/type-aliases/ApiSyllabus.md)

Defined in: [ui/src/api-shared/types/gantt/syllabus-export.ts:12](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/gantt/syllabus-export.ts#L12)

***

### version

> **version**: `"1.0"`

Defined in: [ui/src/api-shared/types/gantt/syllabus-export.ts:8](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/gantt/syllabus-export.ts#L8)
