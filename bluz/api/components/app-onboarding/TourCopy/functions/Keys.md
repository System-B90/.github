[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-onboarding/TourCopy](../index.md) / Keys

# Function: Keys()

> **Keys**(`__namedParameters`): `Element`

Defined in: [ui/src/components/app-onboarding/TourCopy.tsx:31](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/app-onboarding/TourCopy.tsx#L31)

A keyboard shortcut inside Hebrew copy, e.g. `<Keys>Ctrl+K</Keys>`.

Isolated LTR, as docs/ux-guidelines.md §3 asks of Latin text, so "Ctrl+K"
never comes out as "K+Ctrl" mid-sentence — the same reason `MenuShortcut`
renders its hint LTR.

## Parameters

### \_\_namedParameters

#### children

`string`

## Returns

`Element`
