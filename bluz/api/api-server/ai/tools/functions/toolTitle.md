[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/tools](../index.md) / toolTitle

# Function: toolTitle()

> **toolTitle**(`name`): `string`

Defined in: [ui/src/api-server/ai/tools/index.ts:81](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/tools/index.ts#L81)

The human-facing label for a tool name.

Takes a name rather than a tool so that a call to something unregistered —
a model hallucinating `delete_everything` — still renders as text a person
can read instead of a blank chip.

## Parameters

### name

`string`

## Returns

`string`
