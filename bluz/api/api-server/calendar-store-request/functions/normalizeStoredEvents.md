[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/calendar-store-request](../index.md) / normalizeStoredEvents

# Function: normalizeStoredEvents()

> **normalizeStoredEvents**(`events`): [`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

Defined in: [ui/src/api-server/calendar-store-request.ts:10](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/calendar-store-request.ts#L10)

Coerce a request body's `events` field into stored event documents, fixing up
date fields that crossed the wire as strings. Anything else becomes empty.

## Parameters

### events

`unknown`

## Returns

[`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]
