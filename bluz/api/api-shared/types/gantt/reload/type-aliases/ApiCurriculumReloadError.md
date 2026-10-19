[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / ApiCurriculumReloadError

# Type Alias: ApiCurriculumReloadError

> **ApiCurriculumReloadError** = `object`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:125](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L125)

## Properties

### code

> **code**: [`CurriculumReloadErrorCode`](CurriculumReloadErrorCode.md)

Defined in: [ui/src/api-shared/types/gantt/reload.ts:126](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L126)

***

### errors?

> `optional` **errors?**: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]

Defined in: [ui/src/api-shared/types/gantt/reload.ts:128](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L128)

Present for `invalid-plan`: the pure planner's validation errors.

***

### message?

> `optional` **message?**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:129](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L129)
