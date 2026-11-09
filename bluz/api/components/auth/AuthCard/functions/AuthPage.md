[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/auth/AuthCard](../index.md) / AuthPage

# Function: AuthPage()

> **AuthPage**(`__namedParameters`): `Element`

Defined in: [ui/src/components/auth/AuthCard.tsx:14](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/auth/AuthCard.tsx#L14)

The page behind the login, access-denied and CLI-auth cards.

`body` is `h-screen overflow-hidden`, so this box is the only thing that can
scroll. A 100vh page under the 56px pre-auth app bar used to push the card's
bottom (the login button, once an error alert sat above it) off a short
screen with no way to reach it.

## Parameters

### \_\_namedParameters

#### children

`ReactNode`

## Returns

`Element`
