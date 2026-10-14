[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / CurriculumPullBackError

# Class: CurriculumPullBackError

Defined in: [ui/src/api-shared/types/gantt/cut.ts:277](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L277)

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

Defined in: [ui/src/api-shared/types/gantt/cut.ts:283](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L283)

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

Defined in: [ui/src/api-shared/types/gantt/cut.ts:281](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/types/gantt/cut.ts#L281)

#### Implementation of

`ApiCurriculumPullBackError.code`
