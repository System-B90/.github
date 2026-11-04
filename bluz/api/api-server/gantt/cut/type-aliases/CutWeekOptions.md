[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / CutWeekOptions

# Type Alias: CutWeekOptions

> **CutWeekOptions** = [`CutPlanOptions`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanOptions.md) & `object`

Defined in: [ui/src/api-server/gantt/cut.ts:1086](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/cut.ts#L1086)

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
