[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / CurriculumCutError

# Class: CurriculumCutError

Defined in: [ui/src/api-shared/types/gantt/cut.ts:204](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L204)

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

Defined in: [ui/src/api-shared/types/gantt/cut.ts:213](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L213)

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

Defined in: [ui/src/api-shared/types/gantt/cut.ts:208](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L208)

#### Implementation of

`ApiCurriculumCutError.code`

***

### count?

> `readonly` `optional` **count?**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:210](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L210)

Present for `already-cut` (this curriculum's own live cut events) and for
`foreign-cut` (another curriculum's, still live in the same iteration).

#### Implementation of

`ApiCurriculumCutError.count`

***

### errors?

> `readonly` `optional` **errors?**: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]

Defined in: [ui/src/api-shared/types/gantt/cut.ts:209](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L209)

Present for `invalid-plan`: the pure planner's collected validation errors.

#### Implementation of

`ApiCurriculumCutError.errors`

***

### foreignCurriculumId?

> `readonly` `optional` **foreignCurriculumId?**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:211](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L211)

Present for `foreign-cut`: the curriculum whose cut is occupying the iteration.

#### Implementation of

`ApiCurriculumCutError.foreignCurriculumId`
