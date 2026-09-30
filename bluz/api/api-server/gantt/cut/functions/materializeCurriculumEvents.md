[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / materializeCurriculumEvents

# Function: materializeCurriculumEvents()

> **materializeCurriculumEvents**(`curriculum`, `iteration`, `controller`, `options?`): `Promise`\<[`MaterializationOutcome`](../type-aliases/MaterializationOutcome.md)\>

Defined in: [ui/src/api-server/gantt/cut.ts:898](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/cut.ts#L898)

Plan a curriculum and turn the planned occurrences into schedule-event
documents. Shared by the one-shot cut and the reload (#…): both need exactly
the same "what should the schedule look like" computation, and only differ in
what they do with the result.

## Parameters

### curriculum

[`ApiCurriculum`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)

The loaded curriculum tree.

### iteration

The linked iteration (its db supplies settings and courses).

#### dbName

`string`

#### hiveUrl?

`string`

### controller

[`DatabaseController`](../../../mongo-db-controller/classes/DatabaseController.md)

Controller for the iteration database.

### options?

[`CutPlanOptions`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanOptions.md) & `object` = `{}`

## Returns

`Promise`\<[`MaterializationOutcome`](../type-aliases/MaterializationOutcome.md)\>

The intended documents, or the planner's validation errors.
