[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/templates](../index.md) / seedCurriculumFromTemplateWith

# Function: seedCurriculumFromTemplateWith()

> **seedCurriculumFromTemplateWith**(`curriculumId`, `template`, `ops`): `Promise`\<`void`\>

Defined in: [ui/src/api-shared/types/gantt/templates.ts:93](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/gantt/templates.ts#L93)

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
