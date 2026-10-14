[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / CurriculumCutError

# Class: CurriculumCutError

Defined in: [ui/src/api-shared/types/gantt/cut.ts:234](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L234)

Thrown by the client wrapper when a cut is rejected. Carries the full
structured payload (code + planner validation errors + already-cut count)
so the UI can render a specific message or validation list instead of a
generic network error. Extends ClientApiError so it flows through
the shared snackbar handling.

## Extends

- `ClientApiError`

## Implements

- [`ApiCurriculumCutError`](../type-aliases/ApiCurriculumCutError.md)

## Constructors

### Constructor

> **new CurriculumCutError**(`payload`): `CurriculumCutError`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:243](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L243)

#### Parameters

##### payload

[`ApiCurriculumCutError`](../type-aliases/ApiCurriculumCutError.md)

#### Returns

`CurriculumCutError`

#### Overrides

`ClientApiError.constructor`

## Properties

### code

> `readonly` **code**: [`CurriculumCutErrorCode`](../type-aliases/CurriculumCutErrorCode.md)

Defined in: [ui/src/api-shared/types/gantt/cut.ts:238](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L238)

#### Implementation of

`ApiCurriculumCutError.code`

***

### count?

> `readonly` `optional` **count?**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:240](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L240)

Present for `already-cut` (this curriculum's own live cut events) and for
`foreign-cut` (another curriculum's, still live in the same iteration).

#### Implementation of

`ApiCurriculumCutError.count`

***

### errors?

> `readonly` `optional` **errors?**: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]

Defined in: [ui/src/api-shared/types/gantt/cut.ts:239](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L239)

Present for `invalid-plan`: the pure planner's collected validation errors.

#### Implementation of

`ApiCurriculumCutError.errors`

***

### foreignCurriculumId?

> `readonly` `optional` **foreignCurriculumId?**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:241](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L241)

Present for `foreign-cut`: the curriculum whose cut is occupying the iteration.

#### Implementation of

`ApiCurriculumCutError.foreignCurriculumId`
