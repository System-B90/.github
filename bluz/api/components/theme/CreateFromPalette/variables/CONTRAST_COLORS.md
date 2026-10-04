[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/theme/CreateFromPalette](../index.md) / CONTRAST\_COLORS

# Variable: CONTRAST\_COLORS

> `const` **CONTRAST\_COLORS**: `object`

Defined in: [ui/src/components/theme/CreateFromPalette.ts:69](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/theme/CreateFromPalette.ts#L69)

WCAG AA text colours, checked by `tests/backend/theme-contrast.test.ts`.

- The brand turquoise `#67C8DD` is 1.93:1 on white, so it stays a *fill*; in
  light mode text that would have been turquoise uses a darker teal (#807).
- Orange `#ED6C02` is 3.11:1 against white either way round (#827).
- Red `#F44336` is 4.39:1 on the dark paper (#826).

## Type Declaration

### darkError

> `readonly` **darkError**: `"#FF6B5E"` = `"#FF6B5E"`

### darkPrimaryText

> `readonly` **darkPrimaryText**: `"#67C8DD"` = `"#67C8DD"`

### lightPrimaryText

> `readonly` **lightPrimaryText**: `"#1B6F80"` = `"#1B6F80"`

### lightWarning

> `readonly` **lightWarning**: `"#B85300"` = `"#B85300"`
