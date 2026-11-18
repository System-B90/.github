[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/common](../index.md) / aiOrigin

# Function: aiOrigin()

> **aiOrigin**(`context`): [`EventWriteOrigin`](../../../../db-event-history/type-aliases/EventWriteOrigin.md)

Defined in: [ui/src/api-server/ai/tools/common.ts:51](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-server/ai/tools/common.ts#L51)

Marks every assistant write in the event history, so a curious operator can
always tell an AI edit from a human one after the fact.

## Parameters

### context

[`AiToolContext`](../../types/type-aliases/AiToolContext.md)

## Returns

[`EventWriteOrigin`](../../../../db-event-history/type-aliases/EventWriteOrigin.md)
