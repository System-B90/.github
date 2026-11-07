[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-onboarding/anchors](../index.md) / APP\_ANCHORS

# Variable: APP\_ANCHORS

> `const` **APP\_ANCHORS**: `object`

Defined in: [ui/src/components/app-onboarding/anchors.ts:8](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/app-onboarding/anchors.ts#L8)

Every anchor id Bluz spotlights, in one place.

Ids are the contract between a component (which registers one with
`useTourAnchor`) and a tour (which points at one). Naming them here rather
than inline keeps that contract greppable and typo-proof.

## Type Declaration

### help

> `readonly` **help**: `"app.help"` = `"app.help"`

The "?" button: the gantt's status actions, the schedule's toolbar.

### palette

> `readonly` **palette**: `"app.palette"` = `"app.palette"`

The command palette pill in the app bar.

### settings

> `readonly` **settings**: `"app.settings"` = `"app.settings"`

The settings gear in the app bar.

### studentView

> `readonly` **studentView**: `"app.student-view"` = `"app.student-view"`

The student-view preview link in the app bar.
