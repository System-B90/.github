[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/apply-template](../index.md) / seedCurriculumFromTemplate

# Function: seedCurriculumFromTemplate()

> **seedCurriculumFromTemplate**(`curriculumId`, `template`): `Promise`\<`void`\>

Defined in: [ui/src/api-client/gantt/apply-template.ts:16](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-client/gantt/apply-template.ts#L16)

Seeds a (blank) curriculum from a template through the Gantt API.

Used by the "create curriculum from template" flow. It talks to the Gantt API
directly (not the in-memory reducer), so it works before the new curriculum's
provider is mounted.

## Parameters

### curriculumId

`string`

### template

[`GanttCurriculumTemplate`](../../../../api-shared/types/gantt/templates/type-aliases/GanttCurriculumTemplate.md)

## Returns

`Promise`\<`void`\>
