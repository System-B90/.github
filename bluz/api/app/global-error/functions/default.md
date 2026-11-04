[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [app/global-error](../index.md) / default

# Function: default()

> **default**(`__namedParameters`): `Element`

Defined in: [ui/src/app/global-error.tsx:8](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/app/global-error.tsx#L8)

Last line of defence: a throw in the root layout takes the theme providers
down with it, so this page renders its own `<html>`/`<body>` and uses inline
styles only — no MUI, no emotion cache, no fonts to depend on.

## Parameters

### \_\_namedParameters

#### error

`Error` & `object`

#### reset

() => `void`

## Returns

`Element`
