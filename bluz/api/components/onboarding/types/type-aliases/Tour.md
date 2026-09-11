[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/onboarding/types](../index.md) / Tour

# Type Alias: Tour

> **Tour** = `object`

Defined in: [ui/src/components/onboarding/types.ts:50](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L50)

## Properties

### anchorTimeoutMs?

> `optional` **anchorTimeoutMs?**: `number`

Defined in: [ui/src/components/onboarding/types.ts:63](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L63)

How long to wait for a step's anchor to mount, in ms.

***

### autoStart?

> `optional` **autoStart?**: `boolean`

Defined in: [ui/src/components/onboarding/types.ts:61](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L61)

Run once, by itself, the first time it is registered.

***

### id

> **id**: `string`

Defined in: [ui/src/components/onboarding/types.ts:52](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L52)

Stable across releases — it is the persistence key.

***

### steps

> **steps**: [`TourStep`](TourStep.md)[]

Defined in: [ui/src/components/onboarding/types.ts:54](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L54)

***

### title

> **title**: `string`

Defined in: [ui/src/components/onboarding/types.ts:53](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L53)

***

### version?

> `optional` **version?**: `number`

Defined in: [ui/src/components/onboarding/types.ts:59](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L59)

Bump to re-show a tour whose content materially changed. A completion
recorded against an older version no longer counts.
