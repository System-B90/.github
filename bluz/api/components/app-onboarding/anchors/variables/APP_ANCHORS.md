[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-onboarding/anchors](../index.md) / APP\_ANCHORS

# Variable: APP\_ANCHORS

> `const` **APP\_ANCHORS**: `object`

Defined in: [ui/src/components/app-onboarding/anchors.ts:8](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/app-onboarding/anchors.ts#L8)

Every anchor id Bluz spotlights, in one place.

Ids are the contract between a component (which registers one with
`useTourAnchor`) and a tour (which points at one). Naming them here rather
than inline keeps that contract greppable and typo-proof.

## Type Declaration

### help

> `readonly` **help**: `"app.help"` = `"app.help"`

The "?" button in the app bar.
