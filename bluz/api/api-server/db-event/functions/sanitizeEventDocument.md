[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/db-event](../index.md) / sanitizeEventDocument

# Function: sanitizeEventDocument()

> **sanitizeEventDocument**(`event`): [`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)

Defined in: [ui/src/api-server/db-event.ts:106](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/db-event.ts#L106)

A stored-shape event built from an untrusted copy (a snapshot or draft):
allow-listed fields, required arrays present, and the given id.

## Parameters

### event

[`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)

## Returns

[`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)
