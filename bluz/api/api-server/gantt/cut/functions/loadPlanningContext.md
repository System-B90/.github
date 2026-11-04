[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / loadPlanningContext

# Function: loadPlanningContext()

> **loadPlanningContext**(`curriculum`, `iteration`, `controller`, `selection?`): `Promise`\<[`PlanningContext`](../type-aliases/PlanningContext.md)\>

Defined in: [ui/src/api-server/gantt/cut.ts:1369](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/gantt/cut.ts#L1369)

Loads a curriculum's gantt rows, the iteration's courses, the Hive maps and
the week templates, and binds them into a planner. Each week uses the
template it is stamped with in `templateIdByWeekStart`, else `templateId`,
else the default template. The week named by `weekId` takes `templateId`
over its stamp: a single-week reload with a template picked re-plans it
under that template.

## Parameters

### curriculum

[`ApiCurriculum`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)

### iteration

#### hiveUrl?

`string`

### controller

[`DatabaseController`](../../../mongo-db-controller/classes/DatabaseController.md)

### selection?

`Pick`\<[`CutWeekOptions`](../type-aliases/CutWeekOptions.md), `"weekId"` \| `"templateId"` \| `"templateIdByWeekStart"`\> & `object` = `{}`

## Returns

`Promise`\<[`PlanningContext`](../type-aliases/PlanningContext.md)\>
