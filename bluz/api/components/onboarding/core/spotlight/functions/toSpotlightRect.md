[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/onboarding/core/spotlight](../index.md) / toSpotlightRect

# Function: toSpotlightRect()

> **toSpotlightRect**(`element`, `padding`, `viewport`): [`SpotlightRect`](../type-aliases/SpotlightRect.md)

Defined in: [ui/src/components/onboarding/core/spotlight.ts:20](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/core/spotlight.ts#L20)

The anchor's viewport box, grown by `padding` and clipped to the viewport so
a partially off-screen anchor still produces a cutout that is on screen.

## Parameters

### element

`HTMLElement`

### padding

`number`

### viewport

#### height

`number`

#### width

`number`

## Returns

[`SpotlightRect`](../type-aliases/SpotlightRect.md)
