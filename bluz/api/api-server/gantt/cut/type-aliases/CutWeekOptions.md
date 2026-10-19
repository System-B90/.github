[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / CutWeekOptions

# Type Alias: CutWeekOptions

> **CutWeekOptions** = [`CutPlanOptions`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanOptions.md) & `object`

Defined in: [ui/src/api-server/gantt/cut.ts:984](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/cut.ts#L984)

Cut options, optionally limited to one timeline week (#970).

## Type Declaration

### templateId?

> `optional` **templateId?**: `string`

Template for the weeks being cut; the default one when omitted (#997).

### templateIdByWeekStart?

> `optional` **templateIdByWeekStart?**: `Record`\<`string`, `string`\>

Template ids by week Sunday (YYYY-MM-DD), overriding `templateId`: the
templates weeks were cut with, for reloads and template saves.

### weekId?

> `optional` **weekId?**: `string`
