[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/db-event](../index.md) / sanitizeEventDocument

# Function: sanitizeEventDocument()

> **sanitizeEventDocument**(`event`): [`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)

Defined in: [ui/src/api-server/db-event.ts:93](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/db-event.ts#L93)

A stored-shape event built from an untrusted copy (a snapshot or draft):
allow-listed fields, required arrays present, and the given id.

## Parameters

### event

[`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)

## Returns

[`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)
