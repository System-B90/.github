[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / roomKeyOf

# Function: roomKeyOf()

> **roomKeyOf**(`roomName`): `string` \| `null`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:271](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/gantt/cut-rules.ts#L271)

Room identity used by the `room-change` rule. Returns `null` for
"no meaningful room", which never triggers a transition break.
Returns `null` unconditionally while the rule is disabled.

## Parameters

### roomName

`string` \| `null` \| `undefined`

## Returns

`string` \| `null`
