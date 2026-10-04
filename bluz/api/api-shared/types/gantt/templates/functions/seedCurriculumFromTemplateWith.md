[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/templates](../index.md) / seedCurriculumFromTemplateWith

# Function: seedCurriculumFromTemplateWith()

> **seedCurriculumFromTemplateWith**(`curriculumId`, `template`, `ops`): `Promise`\<`void`\>

Defined in: [ui/src/api-shared/types/gantt/templates.ts:93](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/gantt/templates.ts#L93)

Seeds a (blank) curriculum's weeks and per-day working minutes from a
template: exactly `template.weekCount` weeks, each day's
`totalWorkingMinutes` set from the resolved day-config. Only days whose
default differs from the template are written.

## Parameters

### curriculumId

`string`

### template

[`GanttCurriculumTemplate`](../type-aliases/GanttCurriculumTemplate.md)

### ops

[`TemplateSeedOps`](../type-aliases/TemplateSeedOps.md)

## Returns

`Promise`\<`void`\>
