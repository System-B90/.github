[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/BluzCommandPalette](../index.md) / BluzCommandPalette

# Function: BluzCommandPalette()

> **BluzCommandPalette**(`__namedParameters`): `Element`

Defined in: [ui/src/components/app-commands/BluzCommandPalette.tsx:34](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/app-commands/BluzCommandPalette.tsx#L34)

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
