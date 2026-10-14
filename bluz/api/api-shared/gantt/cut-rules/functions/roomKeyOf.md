[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / roomKeyOf

# Function: roomKeyOf()

> **roomKeyOf**(`roomName`): `string` \| `null`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:268](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-rules.ts#L268)

Room identity used by the `room-change` rule. Returns `null` for
"no meaningful room", which never triggers a transition break.
Returns `null` unconditionally while the rule is disabled.

## Parameters

### roomName

`string` \| `null` \| `undefined`

## Returns

`string` \| `null`
