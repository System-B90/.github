[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/NumberSpinner](../index.md) / NumberSpinner

# Function: NumberSpinner()

> **NumberSpinner**(`__namedParameters`): `Element`

Defined in: [ui/src/components/base/NumberSpinner.tsx:59](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/NumberSpinner.tsx#L59)

Duration spinner — for durations only, not general numbers.

`value` / `onValueChange` are always minutes. The דק׳/שעות toggle inside
the field only changes what the user sees and types; the chosen unit is
shared by every spinner and kept in sessionStorage. `step` / `largeStep`
default per unit and, when passed, apply in the shown unit.
`unitToggle={false}` hides the toggle and pins the spinner to minutes.
`label` sits in the top border, like an outlined TextField.
`min` defaults to 0: durations are never negative.

## Parameters

### \_\_namedParameters

`Omit`\<`NumberFieldRootProps`, `"onValueChange"`\> & `object`

## Returns

`Element`
