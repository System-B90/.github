[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/templates](../index.md) / seedCurriculumFromTemplateWith

# Function: seedCurriculumFromTemplateWith()

> **seedCurriculumFromTemplateWith**(`curriculumId`, `template`, `ops`): `Promise`\<`void`\>

Defined in: [ui/src/api-shared/types/gantt/templates.ts:93](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-shared/types/gantt/templates.ts#L93)

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
