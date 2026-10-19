[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / CurriculumPullBackError

# Class: CurriculumPullBackError

Defined in: [ui/src/api-shared/types/gantt/cut.ts:301](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L301)

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

Defined in: [ui/src/api-shared/types/gantt/cut.ts:307](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L307)

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

Defined in: [ui/src/api-shared/types/gantt/cut.ts:305](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L305)

#### Implementation of

`ApiCurriculumPullBackError.code`
