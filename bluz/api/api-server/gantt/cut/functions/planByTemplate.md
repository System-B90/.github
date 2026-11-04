[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / planByTemplate

# Function: planByTemplate()

> **planByTemplate**(`baseInput`, `templateByWeek`, `templates`, `templating`, `plan`): [`CutPlan`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlan.md)

Defined in: [ui/src/api-server/gantt/cut.ts:1297](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/gantt/cut.ts#L1297)

Plans a curriculum whose weeks may use different templates (#997). Weeks
are grouped by template and each group is planned whole, so every week
lands exactly where a plan under its own template puts it; the groups'
weeks are then stitched together. One template is a single plain plan.

## Parameters

### baseInput

[`CutPlanInput`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanInput.md)

### templateByWeek

`Map`\<`string`, `string` \| `undefined`\>

### templates

`Map`\<`string` \| `undefined`, [`CutTemplate`](../../week-template-cut/type-aliases/CutTemplate.md) \| `null`\>

### templating

`Templating`

### plan

(`input`) => [`CutPlan`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlan.md)

## Returns

[`CutPlan`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlan.md)
