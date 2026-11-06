[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / CurriculumPullBackError

# Class: CurriculumPullBackError

Defined in: [ui/src/api-shared/types/gantt/cut.ts:315](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/gantt/cut.ts#L315)

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

Defined in: [ui/src/api-shared/types/gantt/cut.ts:321](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/gantt/cut.ts#L321)

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

Defined in: [ui/src/api-shared/types/gantt/cut.ts:319](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/types/gantt/cut.ts#L319)

#### Implementation of

`ApiCurriculumPullBackError.code`
