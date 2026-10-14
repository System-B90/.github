[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCurriculumCutError

# Type Alias: ApiCurriculumCutError

> **ApiCurriculumCutError** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:212](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L212)

## Properties

### code

> **code**: [`CurriculumCutErrorCode`](CurriculumCutErrorCode.md)

Defined in: [ui/src/api-shared/types/gantt/cut.ts:213](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L213)

***

### count?

> `optional` **count?**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:220](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L220)

Present for `already-cut` (this curriculum's own live cut events) and for
`foreign-cut` (another curriculum's, still live in the same iteration).

***

### errors?

> `optional` **errors?**: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]

Defined in: [ui/src/api-shared/types/gantt/cut.ts:215](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L215)

Present for `invalid-plan`: the pure planner's collected validation errors.

***

### foreignCurriculumId?

> `optional` **foreignCurriculumId?**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:222](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L222)

Present for `foreign-cut`: the curriculum whose cut is occupying the iteration.

***

### message?

> `optional` **message?**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:224](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L224)

Human-readable Hebrew message describing the rejection.
