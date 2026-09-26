[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / CurriculumReloadError

# Class: CurriculumReloadError

Defined in: [ui/src/api-shared/types/gantt/reload.ts:129](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L129)

Thrown by the client wrapper when a reload is rejected, carrying the coded
reason so the dialog renders a specific Hebrew message.

## Extends

- `ClientApiError`

## Implements

- [`ApiCurriculumReloadError`](../type-aliases/ApiCurriculumReloadError.md)

## Constructors

### Constructor

> **new CurriculumReloadError**(`payload`): `CurriculumReloadError`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:136](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L136)

#### Parameters

##### payload

[`ApiCurriculumReloadError`](../type-aliases/ApiCurriculumReloadError.md)

#### Returns

`CurriculumReloadError`

#### Overrides

`ClientApiError.constructor`

## Properties

### code

> `readonly` **code**: [`CurriculumReloadErrorCode`](../type-aliases/CurriculumReloadErrorCode.md)

Defined in: [ui/src/api-shared/types/gantt/reload.ts:133](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L133)

#### Implementation of

`ApiCurriculumReloadError.code`

***

### errors?

> `readonly` `optional` **errors?**: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]

Defined in: [ui/src/api-shared/types/gantt/reload.ts:134](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L134)

Present for `invalid-plan`: the pure planner's validation errors.

#### Implementation of

`ApiCurriculumReloadError.errors`
