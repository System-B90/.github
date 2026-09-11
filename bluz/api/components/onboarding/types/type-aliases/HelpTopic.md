[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/onboarding/types](../index.md) / HelpTopic

# Type Alias: HelpTopic

> **HelpTopic** = `object`

Defined in: [ui/src/components/onboarding/types.ts:67](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L67)

An entry in the persistent help panel.

## Properties

### body

> **body**: `ReactNode`

Defined in: [ui/src/components/onboarding/types.ts:70](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L70)

***

### group?

> `optional` **group?**: `string`

Defined in: [ui/src/components/onboarding/types.ts:72](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L72)

Section heading in the panel. Topics without one land in the default section.

***

### id

> **id**: `string`

Defined in: [ui/src/components/onboarding/types.ts:68](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L68)

***

### order?

> `optional` **order?**: `number`

Defined in: [ui/src/components/onboarding/types.ts:74](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L74)

Lower sorts first within a section. Defaults to registration order.

***

### title

> **title**: `string`

Defined in: [ui/src/components/onboarding/types.ts:69](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L69)

***

### tourId?

> `optional` **tourId?**: `string`

Defined in: [ui/src/components/onboarding/types.ts:76](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L76)

Renders a "replay this tour" action at the end of the topic.
