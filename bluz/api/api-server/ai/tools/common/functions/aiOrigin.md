[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/common](../index.md) / aiOrigin

# Function: aiOrigin()

> **aiOrigin**(`context`): [`EventWriteOrigin`](../../../../db-event-history/type-aliases/EventWriteOrigin.md)

Defined in: [ui/src/api-server/ai/tools/common.ts:51](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-server/ai/tools/common.ts#L51)

Marks every assistant write in the event history, so a curious operator can
always tell an AI edit from a human one after the fact.

## Parameters

### context

[`AiToolContext`](../../types/type-aliases/AiToolContext.md)

## Returns

[`EventWriteOrigin`](../../../../db-event-history/type-aliases/EventWriteOrigin.md)
