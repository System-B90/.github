[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/settings-dialog/tabs/access-tokens/CreateAccessTokenDialog](../index.md) / CreateAccessTokenDialog

# Function: CreateAccessTokenDialog()

> **CreateAccessTokenDialog**(`__namedParameters`): `Element`

Defined in: [ui/src/components/settings-dialog/tabs/access-tokens/CreateAccessTokenDialog.tsx:65](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/settings-dialog/tabs/access-tokens/CreateAccessTokenDialog.tsx#L65)

Two steps in one dialog: the form, then the one-time reveal of the new
secret with copy-paste setup for the CLI/SDK. The reveal cannot be
dismissed by a stray click — the secret is gone once it closes.

## Parameters

### \_\_namedParameters

`CreateAccessTokenDialogProps`

## Returns

`Element`
