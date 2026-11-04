[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / PlanningContext

# Type Alias: PlanningContext

> **PlanningContext** = `object`

Defined in: [ui/src/api-server/gantt/cut.ts:1349](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/gantt/cut.ts#L1349)

Everything planning a curriculum under its week templates needs (#997).

## Properties

### baseInput

> **baseInput**: [`CutPlanInput`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanInput.md)

Defined in: [ui/src/api-server/gantt/cut.ts:1350](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/gantt/cut.ts#L1350)

***

### courses

> **courses**: [`Course`](../../../../api-shared/types/course/type-aliases/Course.md)[]

Defined in: [ui/src/api-server/gantt/cut.ts:1352](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/gantt/cut.ts#L1352)

***

### curriculumIndex

> **curriculumIndex**: `ReturnType`\<*typeof* [`indexCurriculumEvents`](../functions/indexCurriculumEvents.md)\>

Defined in: [ui/src/api-server/gantt/cut.ts:1353](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/gantt/cut.ts#L1353)

***

### hiveModules

> **hiveModules**: `HiveModuleSubjectLookup`

Defined in: [ui/src/api-server/gantt/cut.ts:1354](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/gantt/cut.ts#L1354)

***

### plan

> **plan**: (`planner`) => [`CutPlan`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlan.md)

Defined in: [ui/src/api-server/gantt/cut.ts:1356](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/gantt/cut.ts#L1356)

Plans every week under its own template with the given planner.

#### Parameters

##### planner

(`input`) => [`CutPlan`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlan.md)

#### Returns

[`CutPlan`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlan.md)

***

### templateIdOfDate

> **templateIdOfDate**: (`date`) => `string` \| `undefined`

Defined in: [ui/src/api-server/gantt/cut.ts:1358](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/gantt/cut.ts#L1358)

The template id a dated occurrence's week is planned with.

#### Parameters

##### date

`string`

#### Returns

`string` \| `undefined`

***

### weeks

> **weeks**: [`ApiCutWeek`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCutWeek.md)[]

Defined in: [ui/src/api-server/gantt/cut.ts:1351](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/gantt/cut.ts#L1351)
