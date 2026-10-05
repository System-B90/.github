[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/use-command](../index.md) / useCommand

# Function: useCommand()

> **useCommand**(`command`): `void`

Defined in: [ui/src/components/app-commands/use-command.ts:15](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/app-commands/use-command.ts#L15)

Mirror a single on-screen control in the palette.

The owning component passes the same handler its button calls, so the two
can never drift apart. Memoised on the command's primitive fields rather than
its identity, so callers can build the object inline every render; `icon` is
read from whichever render last changed one of those fields.

Pass `null` to contribute nothing (e.g. when the owner has no subject yet).

## Parameters

### command

`Command` \| `null`

## Returns

`void`
