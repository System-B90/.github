[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/anthropic-messages](../index.md) / toWireRequest

# Function: toWireRequest()

> **toWireRequest**(`messages`): `object`

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:120](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/ai/anthropic-messages.ts#L120)

Maps Bluz's transcript onto the wire: system text goes top-level, tool
results ride in user turns, and same-role neighbours merge — the wire wants
strictly alternating turns, and every result of one assistant turn in the
single user turn after it.

## Parameters

### messages

[`AiMessage`](../../../../api-shared/types/ai/type-aliases/AiMessage.md)[]

## Returns

`object`

### messages

> **messages**: `OutMessage`[]

### system?

> `optional` **system?**: `string`
