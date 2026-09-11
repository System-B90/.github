[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/onboarding/OnboardingProvider](../index.md) / OnboardingProviderProps

# Type Alias: OnboardingProviderProps

> **OnboardingProviderProps** = `object`

Defined in: [ui/src/components/onboarding/OnboardingProvider.tsx:39](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingProvider.tsx#L39)

## Properties

### autoStart?

> `optional` **autoStart?**: `boolean`

Defined in: [ui/src/components/onboarding/OnboardingProvider.tsx:48](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingProvider.tsx#L48)

Set `false` to require every tour to be started by hand.

***

### children

> **children**: `ReactNode`

Defined in: [ui/src/components/onboarding/OnboardingProvider.tsx:40](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingProvider.tsx#L40)

***

### labels

> **labels**: [`OnboardingLabels`](../../types/type-aliases/OnboardingLabels.md)

Defined in: [ui/src/components/onboarding/OnboardingProvider.tsx:42](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingProvider.tsx#L42)

The copy table. Must be referentially stable.

***

### onTourEnd?

> `optional` **onTourEnd?**: (`tourId`, `reason`) => `void`

Defined in: [ui/src/components/onboarding/OnboardingProvider.tsx:49](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingProvider.tsx#L49)

#### Parameters

##### tourId

`string`

##### reason

[`TourEndReason`](../../types/type-aliases/TourEndReason.md)

#### Returns

`void`

***

### storage?

> `optional` **storage?**: [`OnboardingStorage`](../../types/type-aliases/OnboardingStorage.md)

Defined in: [ui/src/components/onboarding/OnboardingProvider.tsx:46](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingProvider.tsx#L46)

Swap in a server-backed store to make "seen" follow the user.

***

### storageNamespace

> **storageNamespace**: `string`

Defined in: [ui/src/components/onboarding/OnboardingProvider.tsx:44](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/OnboardingProvider.tsx#L44)

Prefix for persisted keys — one per app, so two apps never collide.
