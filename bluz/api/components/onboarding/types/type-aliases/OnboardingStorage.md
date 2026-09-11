[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/onboarding/types](../index.md) / OnboardingStorage

# Type Alias: OnboardingStorage

> **OnboardingStorage** = `object`

Defined in: [ui/src/components/onboarding/types.ts:105](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L105)

Storage seam. Swap it for a server-backed profile without touching the UI.

## Properties

### read

> **read**: (`key`) => `null` \| `string`

Defined in: [ui/src/components/onboarding/types.ts:106](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L106)

#### Parameters

##### key

`string`

#### Returns

`null` \| `string`

***

### write

> **write**: (`key`, `value`) => `void`

Defined in: [ui/src/components/onboarding/types.ts:107](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L107)

#### Parameters

##### key

`string`

##### value

`string`

#### Returns

`void`
