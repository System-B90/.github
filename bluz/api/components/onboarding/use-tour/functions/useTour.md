[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/onboarding/use-tour](../index.md) / useTour

# Function: useTour()

> **useTour**(`tour`): `void`

Defined in: [ui/src/components/onboarding/use-tour.ts:15](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-tour.ts#L15)

Contributes a tour from the component that owns the screen it describes, so
the tour is registered exactly while that screen is mounted.

`tour` must be referentially stable — a module constant, or `useMemo` with
the callbacks its steps close over. A fresh object every render re-registers
the tour every render.

## Parameters

### tour

[`Tour`](../../types/type-aliases/Tour.md)

## Returns

`void`
