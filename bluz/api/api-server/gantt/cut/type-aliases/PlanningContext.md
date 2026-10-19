[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / PlanningContext

# Type Alias: PlanningContext

> **PlanningContext** = `object`

Defined in: [ui/src/api-server/gantt/cut.ts:1225](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/cut.ts#L1225)

Everything planning a curriculum under its week templates needs (#997).

## Properties

### baseInput

> **baseInput**: [`CutPlanInput`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanInput.md)

Defined in: [ui/src/api-server/gantt/cut.ts:1226](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/cut.ts#L1226)

***

### courses

> **courses**: [`Course`](../../../../api-shared/types/course/type-aliases/Course.md)[]

Defined in: [ui/src/api-server/gantt/cut.ts:1228](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/cut.ts#L1228)

***

### curriculumIndex

> **curriculumIndex**: `ReturnType`\<*typeof* [`indexCurriculumEvents`](../functions/indexCurriculumEvents.md)\>

Defined in: [ui/src/api-server/gantt/cut.ts:1229](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/cut.ts#L1229)

***

### hiveModules

> **hiveModules**: `HiveModuleSubjectLookup`

Defined in: [ui/src/api-server/gantt/cut.ts:1230](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/cut.ts#L1230)

***

### plan

> **plan**: (`planner`) => [`CutPlan`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlan.md)

Defined in: [ui/src/api-server/gantt/cut.ts:1232](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/cut.ts#L1232)

Plans every week under its own template with the given planner.

#### Parameters

##### planner

(`input`) => [`CutPlan`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlan.md)

#### Returns

[`CutPlan`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlan.md)

***

### templateIdOfDate

> **templateIdOfDate**: (`date`) => `string` \| `undefined`

Defined in: [ui/src/api-server/gantt/cut.ts:1234](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/cut.ts#L1234)

The template id a dated occurrence's week is planned with.

#### Parameters

##### date

`string`

#### Returns

`string` \| `undefined`

***

### weeks

> **weeks**: [`ApiCutWeek`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCutWeek.md)[]

Defined in: [ui/src/api-server/gantt/cut.ts:1227](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/cut.ts#L1227)
