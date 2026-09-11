[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/onboarding/OnboardingContext](../index.md) / OnboardingContextValue

# Type Alias: OnboardingContextValue

> **OnboardingContextValue** = `object`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:13](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L13)

## Properties

### activeStep

> **activeStep**: `null` \| [`TourStep`](../../types/type-aliases/TourStep.md)

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:20](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L20)

***

### activeStepIndex

> **activeStepIndex**: `number`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:21](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L21)

***

### activeTour

> **activeTour**: `null` \| [`Tour`](../../types/type-aliases/Tour.md)

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:19](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L19)

The running tour, or `null`.

***

### closeHelp

> **closeHelp**: () => `void`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:44](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L44)

#### Returns

`void`

***

### endTour

> **endTour**: (`reason`) => `void`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:24](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L24)

#### Parameters

##### reason

[`TourEndReason`](../../types/type-aliases/TourEndReason.md)

#### Returns

`void`

***

### forgetTour

> **forgetTour**: (`tourId`) => `void`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:40](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L40)

Forgets a tour's completion, so it auto-starts again.

#### Parameters

##### tourId

`string`

#### Returns

`void`

***

### goToNextStep

> **goToNextStep**: () => `void`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L25)

#### Returns

`void`

***

### goToPreviousStep

> **goToPreviousStep**: () => `void`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:26](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L26)

#### Returns

`void`

***

### isFirstStep

> **isFirstStep**: `boolean`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:30](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L30)

`true` while no earlier step is showable.

***

### isHelpOpen

> **isHelpOpen**: `boolean`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:42](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L42)

***

### isLastStep

> **isLastStep**: `boolean`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:28](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L28)

`true` while the current step is the last one this run will show.

***

### isTourCompleted

> **isTourCompleted**: (`tourId`) => `boolean`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:38](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L38)

#### Parameters

##### tourId

`string`

#### Returns

`boolean`

***

### labels

> **labels**: [`OnboardingLabels`](../../types/type-aliases/OnboardingLabels.md)

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:14](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L14)

***

### openHelp

> **openHelp**: () => `void`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:43](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L43)

#### Returns

`void`

***

### registerTopics

> **registerTopics**: (`topics`) => () => `void`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:36](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L36)

#### Parameters

##### topics

`ReadonlyArray`\<[`HelpTopic`](../../types/type-aliases/HelpTopic.md)\>

#### Returns

() => `void`

***

### registerTour

> **registerTour**: (`tour`) => () => `void`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:35](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L35)

#### Parameters

##### tour

[`Tour`](../../types/type-aliases/Tour.md)

#### Returns

() => `void`

***

### registry

> **registry**: [`AnchorRegistry`](../../core/anchors/classes/AnchorRegistry.md)

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L16)

Live anchor id → element map. Written by `useTourAnchor`.

***

### startTour

> **startTour**: (`tourId`) => `void`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:23](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L23)

#### Parameters

##### tourId

`string`

#### Returns

`void`

***

### stepCounter

> **stepCounter**: `object`

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:31](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L31)

#### current

> **current**: `number`

#### total

> **total**: `number`

***

### topics

> **topics**: `ReadonlyArray`\<[`HelpTopic`](../../types/type-aliases/HelpTopic.md)\>

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:34](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L34)

***

### tours

> **tours**: `ReadonlyMap`\<`string`, [`Tour`](../../types/type-aliases/Tour.md)\>

Defined in: [ui/src/components/onboarding/OnboardingContext.ts:33](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingContext.ts#L33)
