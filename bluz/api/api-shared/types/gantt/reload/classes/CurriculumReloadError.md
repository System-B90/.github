[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / CurriculumReloadError

# Class: CurriculumReloadError

Defined in: [ui/src/api-shared/types/gantt/reload.ts:136](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/reload.ts#L136)

Thrown by the client wrapper when a reload is rejected, carrying the coded
reason so the dialog renders a specific Hebrew message.

## Extends

- `ClientApiError`

## Implements

- [`ApiCurriculumReloadError`](../type-aliases/ApiCurriculumReloadError.md)

## Constructors

### Constructor

> **new CurriculumReloadError**(`payload`): `CurriculumReloadError`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:143](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/reload.ts#L143)

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

Defined in: [ui/src/api-shared/types/gantt/reload.ts:140](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/reload.ts#L140)

#### Implementation of

`ApiCurriculumReloadError.code`

***

### errors?

> `readonly` `optional` **errors?**: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]

Defined in: [ui/src/api-shared/types/gantt/reload.ts:141](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/reload.ts#L141)

Present for `invalid-plan`: the pure planner's validation errors.

#### Implementation of

`ApiCurriculumReloadError.errors`
