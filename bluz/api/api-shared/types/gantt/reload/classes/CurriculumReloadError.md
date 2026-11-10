[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / CurriculumReloadError

# Class: CurriculumReloadError

Defined in: [ui/src/api-shared/types/gantt/reload.ts:146](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/gantt/reload.ts#L146)

Thrown by the client wrapper when a reload is rejected, carrying the coded
reason so the dialog renders a specific Hebrew message.

## Extends

- `ClientApiError`

## Implements

- [`ApiCurriculumReloadError`](../type-aliases/ApiCurriculumReloadError.md)

## Constructors

### Constructor

> **new CurriculumReloadError**(`payload`): `CurriculumReloadError`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:153](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/gantt/reload.ts#L153)

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

Defined in: [ui/src/api-shared/types/gantt/reload.ts:150](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/gantt/reload.ts#L150)

#### Implementation of

`ApiCurriculumReloadError.code`

***

### errors?

> `readonly` `optional` **errors?**: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]

Defined in: [ui/src/api-shared/types/gantt/reload.ts:151](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/gantt/reload.ts#L151)

Present for `invalid-plan`: the pure planner's validation errors.

#### Implementation of

`ApiCurriculumReloadError.errors`
