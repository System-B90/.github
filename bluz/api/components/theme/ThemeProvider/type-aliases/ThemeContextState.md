[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/theme/ThemeProvider](../index.md) / ThemeContextState

# Type Alias: ThemeContextState

> **ThemeContextState** = `object`

Defined in: [ui/src/components/theme/ThemeProvider.tsx:53](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/theme/ThemeProvider.tsx#L53)

## Properties

### accent

> **accent**: [`Accent`](Accent.md)

Defined in: [ui/src/components/theme/ThemeProvider.tsx:56](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/theme/ThemeProvider.tsx#L56)

***

### resolvedTheme

> **resolvedTheme**: [`Brightness`](Brightness.md)

Defined in: [ui/src/components/theme/ThemeProvider.tsx:55](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/theme/ThemeProvider.tsx#L55)

Brightness only: pink is light, pink-dark is dark.

***

### setAccent

> **setAccent**: (`accent`) => `void`

Defined in: [ui/src/components/theme/ThemeProvider.tsx:62](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/theme/ThemeProvider.tsx#L62)

Switches brand/pink and keeps the current brightness.

#### Parameters

##### accent

[`Accent`](Accent.md)

#### Returns

`void`

***

### setBrightness

> **setBrightness**: (`brightness`) => `void`

Defined in: [ui/src/components/theme/ThemeProvider.tsx:60](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/theme/ThemeProvider.tsx#L60)

Switches light/dark and keeps the current accent.

#### Parameters

##### brightness

[`Brightness`](Brightness.md)

#### Returns

`void`

***

### setTheme

> **setTheme**: (`theme`) => `void`

Defined in: [ui/src/components/theme/ThemeProvider.tsx:58](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/theme/ThemeProvider.tsx#L58)

#### Parameters

##### theme

[`ThemeMode`](ThemeMode.md)

#### Returns

`void`

***

### theme

> **theme**: [`ThemeMode`](ThemeMode.md)

Defined in: [ui/src/components/theme/ThemeProvider.tsx:57](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/theme/ThemeProvider.tsx#L57)
