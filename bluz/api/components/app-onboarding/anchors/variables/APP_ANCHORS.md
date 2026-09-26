[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-onboarding/anchors](../index.md) / APP\_ANCHORS

# Variable: APP\_ANCHORS

> `const` **APP\_ANCHORS**: `object`

Defined in: [ui/src/components/app-onboarding/anchors.ts:8](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/app-onboarding/anchors.ts#L8)

Every anchor id Bluz spotlights, in one place.

Ids are the contract between a component (which registers one with
`useTourAnchor`) and a tour (which points at one). Naming them here rather
than inline keeps that contract greppable and typo-proof.

## Type Declaration

### help

> `readonly` **help**: `"app.help"` = `"app.help"`

The "?" button in the app bar.
