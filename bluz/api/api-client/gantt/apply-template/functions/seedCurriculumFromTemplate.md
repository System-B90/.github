[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/apply-template](../index.md) / seedCurriculumFromTemplate

# Function: seedCurriculumFromTemplate()

> **seedCurriculumFromTemplate**(`curriculumId`, `template`): `Promise`\<`void`\>

Defined in: [ui/src/api-client/gantt/apply-template.ts:19](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/apply-template.ts#L19)

Seeds a (blank) curriculum's weeks and per-day working minutes from a
template. Creates exactly `template.weekCount` weeks; each newly created week
comes back with its linked days, whose `totalWorkingMinutes` we set from the
template's resolved day-config.

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
