[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/apply-template](../index.md) / seedCurriculumFromTemplate

# Function: seedCurriculumFromTemplate()

> **seedCurriculumFromTemplate**(`curriculumId`, `template`): `Promise`\<`void`\>

Defined in: [ui/src/api-client/gantt/apply-template.ts:16](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-client/gantt/apply-template.ts#L16)

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
