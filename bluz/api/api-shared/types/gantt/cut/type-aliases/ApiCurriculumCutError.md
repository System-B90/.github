[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCurriculumCutError

# Type Alias: ApiCurriculumCutError

> **ApiCurriculumCutError** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:182](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/cut.ts#L182)

## Properties

### code

> **code**: [`CurriculumCutErrorCode`](CurriculumCutErrorCode.md)

Defined in: [ui/src/api-shared/types/gantt/cut.ts:183](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/cut.ts#L183)

***

### count?

> `optional` **count?**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:190](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/cut.ts#L190)

Present for `already-cut` (this curriculum's own live cut events) and for
`foreign-cut` (another curriculum's, still live in the same iteration).

***

### errors?

> `optional` **errors?**: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]

Defined in: [ui/src/api-shared/types/gantt/cut.ts:185](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/cut.ts#L185)

Present for `invalid-plan`: the pure planner's collected validation errors.

***

### foreignCurriculumId?

> `optional` **foreignCurriculumId?**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:192](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/cut.ts#L192)

Present for `foreign-cut`: the curriculum whose cut is occupying the iteration.

***

### message?

> `optional` **message?**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:194](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/cut.ts#L194)

Human-readable Hebrew message describing the rejection.
