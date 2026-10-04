[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/common](../index.md) / aiOrigin

# Function: aiOrigin()

> **aiOrigin**(`context`): [`EventWriteOrigin`](../../../../db-event-history/type-aliases/EventWriteOrigin.md)

Defined in: [ui/src/api-server/ai/tools/common.ts:50](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/tools/common.ts#L50)

Marks every assistant write in the event history, so a curious operator can
always tell an AI edit from a human one after the fact.

## Parameters

### context

[`AiToolContext`](../../types/type-aliases/AiToolContext.md)

## Returns

[`EventWriteOrigin`](../../../../db-event-history/type-aliases/EventWriteOrigin.md)
