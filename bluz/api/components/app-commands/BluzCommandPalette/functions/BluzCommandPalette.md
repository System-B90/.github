[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/BluzCommandPalette](../index.md) / BluzCommandPalette

# Function: BluzCommandPalette()

> **BluzCommandPalette**(`__namedParameters`): `Element`

Defined in: [ui/src/components/app-commands/BluzCommandPalette.tsx:34](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/app-commands/BluzCommandPalette.tsx#L34)

Bluz's palette. Wraps the generic package with this app's copy and its
app-wide commands.

Must be mounted inside the data providers the app-wide commands read from
(rooms, outsiders, theme) and outside everything that contributes commands of
its own — which in practice means inside the post-auth layout.

## Parameters

### \_\_namedParameters

#### children

`ReactNode`

## Returns

`Element`
