[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / loadPlanningContext

# Function: loadPlanningContext()

> **loadPlanningContext**(`curriculum`, `iteration`, `controller`, `selection?`): `Promise`\<[`PlanningContext`](../type-aliases/PlanningContext.md)\>

Defined in: [ui/src/api-server/gantt/cut.ts:1243](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/gantt/cut.ts#L1243)

Loads a curriculum's gantt rows, the iteration's courses, the Hive maps and
the week templates, and binds them into a planner. Each week uses the
template it is assigned in `templateIdByWeekId`, else `templateId`, else
the default template.

## Parameters

### curriculum

[`ApiCurriculum`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)

### iteration

#### hiveUrl?

`string`

### controller

[`DatabaseController`](../../../mongo-db-controller/classes/DatabaseController.md)

### selection?

`Pick`\<[`CutWeekOptions`](../type-aliases/CutWeekOptions.md), `"templateId"` \| `"templateIdByWeekStart"`\> & `object` = `{}`

## Returns

`Promise`\<[`PlanningContext`](../type-aliases/PlanningContext.md)\>
