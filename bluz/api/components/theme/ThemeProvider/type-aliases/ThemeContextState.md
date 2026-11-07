[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/theme/ThemeProvider](../index.md) / ThemeContextState

# Type Alias: ThemeContextState

> **ThemeContextState** = `object`

Defined in: [ui/src/components/theme/ThemeProvider.tsx:54](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/theme/ThemeProvider.tsx#L54)

## Properties

### accent

> **accent**: [`Accent`](Accent.md)

Defined in: [ui/src/components/theme/ThemeProvider.tsx:57](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/theme/ThemeProvider.tsx#L57)

***

### resolvedTheme

> **resolvedTheme**: [`Brightness`](Brightness.md)

Defined in: [ui/src/components/theme/ThemeProvider.tsx:56](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/theme/ThemeProvider.tsx#L56)

Brightness only: pink is light, pink-dark is dark.

***

### setAccent

> **setAccent**: (`accent`) => `void`

Defined in: [ui/src/components/theme/ThemeProvider.tsx:63](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/theme/ThemeProvider.tsx#L63)

Switches brand/pink and keeps the current brightness.

#### Parameters

##### accent

[`Accent`](Accent.md)

#### Returns

`void`

***

### setBrightness

> **setBrightness**: (`brightness`) => `void`

Defined in: [ui/src/components/theme/ThemeProvider.tsx:61](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/theme/ThemeProvider.tsx#L61)

Switches light/dark and keeps the current accent.

#### Parameters

##### brightness

[`Brightness`](Brightness.md)

#### Returns

`void`

***

### setTheme

> **setTheme**: (`theme`) => `void`

Defined in: [ui/src/components/theme/ThemeProvider.tsx:59](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/theme/ThemeProvider.tsx#L59)

#### Parameters

##### theme

[`ThemeMode`](ThemeMode.md)

#### Returns

`void`

***

### theme

> **theme**: [`ThemeMode`](ThemeMode.md)

Defined in: [ui/src/components/theme/ThemeProvider.tsx:58](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/theme/ThemeProvider.tsx#L58)
