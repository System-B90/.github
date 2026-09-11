[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/onboarding/core/steps](../index.md) / findShowableStep

# Function: findShowableStep()

> **findShowableStep**(`steps`, `from`, `direction`, `canShow`): `number` \| `null`

Defined in: [ui/src/components/onboarding/core/steps.ts:13](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/core/steps.ts#L13)

The next index in `direction` whose step can actually be shown, or `null`
when the tour runs off either end.

Steps are skipped, not stalled on: a step marked `optional` whose anchor is
nowhere on screen is simply not part of this run — which is what lets one
tour describe UI that only some users, or some states, ever render.

## Parameters

### steps

[`TourStep`](../../../types/type-aliases/TourStep.md)[]

### from

`number`

### direction

[`StepDirection`](../type-aliases/StepDirection.md)

### canShow

(`step`) => `boolean`

## Returns

`number` \| `null`
