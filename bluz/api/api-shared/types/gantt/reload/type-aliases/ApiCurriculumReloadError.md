[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / ApiCurriculumReloadError

# Type Alias: ApiCurriculumReloadError

> **ApiCurriculumReloadError** = `object`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:118](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/gantt/reload.ts#L118)

## Properties

### code

> **code**: [`CurriculumReloadErrorCode`](CurriculumReloadErrorCode.md)

Defined in: [ui/src/api-shared/types/gantt/reload.ts:119](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/gantt/reload.ts#L119)

***

### errors?

> `optional` **errors?**: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]

Defined in: [ui/src/api-shared/types/gantt/reload.ts:121](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/gantt/reload.ts#L121)

Present for `invalid-plan`: the pure planner's validation errors.

***

### message?

> `optional` **message?**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:122](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/gantt/reload.ts#L122)
