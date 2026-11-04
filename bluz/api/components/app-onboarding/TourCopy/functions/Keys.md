[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-onboarding/TourCopy](../index.md) / Keys

# Function: Keys()

> **Keys**(`__namedParameters`): `Element`

Defined in: [ui/src/components/app-onboarding/TourCopy.tsx:31](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/app-onboarding/TourCopy.tsx#L31)

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
