[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / roomKeyOf

# Function: roomKeyOf()

> **roomKeyOf**(`roomName`): `string` \| `null`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:271](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/cut-rules.ts#L271)

Room identity used by the `room-change` rule. Returns `null` for
"no meaningful room", which never triggers a transition break.
Returns `null` unconditionally while the rule is disabled.

## Parameters

### roomName

`string` \| `null` \| `undefined`

## Returns

`string` \| `null`
