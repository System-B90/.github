[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / CurriculumPullBackError

# Class: CurriculumPullBackError

Defined in: [ui/src/api-shared/types/gantt/cut.ts:247](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L247)

Thrown by the client wrapper when a pull-back is rejected. Carries the coded
reason (no linked iteration / nothing to pull back) so the dialog can render
a specific Hebrew message instead of a generic network error.

## Extends

- `ClientApiError`

## Implements

- [`ApiCurriculumPullBackError`](../type-aliases/ApiCurriculumPullBackError.md)

## Constructors

### Constructor

> **new CurriculumPullBackError**(`payload`): `CurriculumPullBackError`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:253](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L253)

#### Parameters

##### payload

[`ApiCurriculumPullBackError`](../type-aliases/ApiCurriculumPullBackError.md)

#### Returns

`CurriculumPullBackError`

#### Overrides

`ClientApiError.constructor`

## Properties

### code

> `readonly` **code**: [`CurriculumPullBackErrorCode`](../type-aliases/CurriculumPullBackErrorCode.md)

Defined in: [ui/src/api-shared/types/gantt/cut.ts:251](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L251)

#### Implementation of

`ApiCurriculumPullBackError.code`
