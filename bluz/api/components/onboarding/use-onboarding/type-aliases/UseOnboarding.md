[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/onboarding/use-onboarding](../index.md) / UseOnboarding

# Type Alias: UseOnboarding

> **UseOnboarding** = `object`

Defined in: [ui/src/components/onboarding/use-onboarding.ts:10](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-onboarding.ts#L10)

## Properties

### activeTour

> **activeTour**: `null` \| [`Tour`](../../types/type-aliases/Tour.md)

Defined in: [ui/src/components/onboarding/use-onboarding.ts:12](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-onboarding.ts#L12)

***

### closeHelp

> **closeHelp**: () => `void`

Defined in: [ui/src/components/onboarding/use-onboarding.ts:21](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-onboarding.ts#L21)

#### Returns

`void`

***

### endTour

> **endTour**: (`reason`) => `void`

Defined in: [ui/src/components/onboarding/use-onboarding.ts:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-onboarding.ts#L16)

#### Parameters

##### reason

[`TourEndReason`](../../types/type-aliases/TourEndReason.md)

#### Returns

`void`

***

### forgetTour

> **forgetTour**: (`tourId`) => `void`

Defined in: [ui/src/components/onboarding/use-onboarding.ts:18](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-onboarding.ts#L18)

#### Parameters

##### tourId

`string`

#### Returns

`void`

***

### isHelpOpen

> **isHelpOpen**: `boolean`

Defined in: [ui/src/components/onboarding/use-onboarding.ts:19](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-onboarding.ts#L19)

***

### isTourCompleted

> **isTourCompleted**: (`tourId`) => `boolean`

Defined in: [ui/src/components/onboarding/use-onboarding.ts:17](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-onboarding.ts#L17)

#### Parameters

##### tourId

`string`

#### Returns

`boolean`

***

### labels

> **labels**: [`OnboardingLabels`](../../types/type-aliases/OnboardingLabels.md)

Defined in: [ui/src/components/onboarding/use-onboarding.ts:11](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-onboarding.ts#L11)

***

### openHelp

> **openHelp**: () => `void`

Defined in: [ui/src/components/onboarding/use-onboarding.ts:20](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-onboarding.ts#L20)

#### Returns

`void`

***

### startTour

> **startTour**: (`tourId`) => `void`

Defined in: [ui/src/components/onboarding/use-onboarding.ts:15](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-onboarding.ts#L15)

#### Parameters

##### tourId

`string`

#### Returns

`void`

***

### topics

> **topics**: `ReadonlyArray`\<[`HelpTopic`](../../types/type-aliases/HelpTopic.md)\>

Defined in: [ui/src/components/onboarding/use-onboarding.ts:14](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-onboarding.ts#L14)

***

### tours

> **tours**: `ReadonlyMap`\<`string`, [`Tour`](../../types/type-aliases/Tour.md)\>

Defined in: [ui/src/components/onboarding/use-onboarding.ts:13](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-onboarding.ts#L13)
