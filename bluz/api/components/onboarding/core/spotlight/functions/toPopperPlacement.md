[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/onboarding/core/spotlight](../index.md) / toPopperPlacement

# Function: toPopperPlacement()

> **toPopperPlacement**(`placement`, `direction`): `"left"` \| `"right"` \| `"top"` \| `"bottom"`

Defined in: [ui/src/components/onboarding/core/spotlight.ts:62](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/core/spotlight.ts#L62)

Resolves a logical placement against the document's direction. Popper speaks
physical sides only, and letting it flip `start`/`end` itself would fight the
app's own RTL handling.

## Parameters

### placement

[`TourPlacement`](../../../types/type-aliases/TourPlacement.md) \| `undefined`

### direction

`"rtl"` \| `"ltr"`

## Returns

`"left"` \| `"right"` \| `"top"` \| `"bottom"`
