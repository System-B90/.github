[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/onboarding/types](../index.md) / TourStep

# Type Alias: TourStep

> **TourStep** = `object`

Defined in: [ui/src/components/onboarding/types.ts:22](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L22)

## Properties

### anchor?

> `optional` **anchor?**: [`TourAnchorId`](TourAnchorId.md)

Defined in: [ui/src/components/onboarding/types.ts:28](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L28)

Element to spotlight. Omit for a centred, anchor-less step.

***

### beforeShow?

> `optional` **beforeShow?**: () => `Promise`\<`void`\> \| `void`

Defined in: [ui/src/components/onboarding/types.ts:36](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L36)

Ran before the step is shown, and awaited. This is how a tour opens the
drawer or switches to the tab that holds the next anchor.

#### Returns

`Promise`\<`void`\> \| `void`

***

### body

> **body**: `ReactNode`

Defined in: [ui/src/components/onboarding/types.ts:26](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L26)

***

### id

> **id**: `string`

Defined in: [ui/src/components/onboarding/types.ts:24](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L24)

Unique within its tour. Used as the React key and in analytics.

***

### interactive?

> `optional` **interactive?**: `boolean`

Defined in: [ui/src/components/onboarding/types.ts:41](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L41)

Leaves the spotlighted element clickable through the overlay, so a step
can invite the user to press the control it is describing.

***

### optional?

> `optional` **optional?**: `boolean`

Defined in: [ui/src/components/onboarding/types.ts:47](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L47)

When the anchor never appears, an optional step is skipped instead of
degrading to a centred card. Use it for steps about UI that only exists
in some states.

***

### padding?

> `optional` **padding?**: `number`

Defined in: [ui/src/components/onboarding/types.ts:31](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L31)

Extra space, in px, between the anchor's box and the cutout's edge.

***

### placement?

> `optional` **placement?**: [`TourPlacement`](TourPlacement.md)

Defined in: [ui/src/components/onboarding/types.ts:29](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L29)

***

### title

> **title**: `string`

Defined in: [ui/src/components/onboarding/types.ts:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/types.ts#L25)
