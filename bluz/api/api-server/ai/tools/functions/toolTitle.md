[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/tools](../index.md) / toolTitle

# Function: toolTitle()

> **toolTitle**(`name`): `string`

Defined in: [ui/src/api-server/ai/tools/index.ts:84](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/ai/tools/index.ts#L84)

The human-facing label for a tool name.

Takes a name rather than a tool so that a call to something unregistered —
a model hallucinating `delete_everything` — still renders as text a person
can read instead of a blank chip.

## Parameters

### name

`string`

## Returns

`string`
