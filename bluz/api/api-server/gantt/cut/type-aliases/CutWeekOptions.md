[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / CutWeekOptions

# Type Alias: CutWeekOptions

> **CutWeekOptions** = [`CutPlanOptions`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanOptions.md) & `object`

Defined in: [ui/src/api-server/gantt/cut.ts:1086](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/gantt/cut.ts#L1086)

Cut options, optionally limited to one timeline week (#970).

## Type Declaration

### assignInstructors?

> `optional` **assignInstructors?**: `boolean`

Place each event's orchestrator as its instructor. Defaults to on.

### templateId?

> `optional` **templateId?**: `string`

Template for the weeks being cut; the default one when omitted (#997).

### templateIdByWeekStart?

> `optional` **templateIdByWeekStart?**: `Record`\<`string`, `string`\>

Template ids by week Sunday (YYYY-MM-DD), overriding `templateId`: the
templates weeks were cut with, for reloads and template saves.

### weekId?

> `optional` **weekId?**: `string`
