[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/theme/CreateFromPalette](../index.md) / CONTRAST\_COLORS

# Variable: CONTRAST\_COLORS

> `const` **CONTRAST\_COLORS**: `object`

Defined in: [ui/src/components/theme/CreateFromPalette.ts:43](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/theme/CreateFromPalette.ts#L43)

Text colors, checked by `tests/backend/theme-contrast.test.ts`.

- Light mode keeps the brand turquoise `#67C8DD` and orange `#ED6C02` as
  text and icon colors; darkening them made the app look worse (#938).
- Red `#F44336` is 4.39:1 on the dark paper, so dark mode lightens it (#826).

## Type Declaration

### darkError

> `readonly` **darkError**: `"#FF6B5E"` = `"#FF6B5E"`

### darkPrimaryText

> `readonly` **darkPrimaryText**: `"#67C8DD"` = `"#67C8DD"`

### lightPrimaryText

> `readonly` **lightPrimaryText**: `"#67C8DD"` = `"#67C8DD"`

### lightWarning

> `readonly` **lightWarning**: `"#ED6C02"` = `"#ED6C02"`
