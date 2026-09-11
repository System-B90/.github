[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/calendar-store-request](../index.md) / normalizeStoredEvents

# Function: normalizeStoredEvents()

> **normalizeStoredEvents**(`events`): [`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

Defined in: [ui/src/api-server/calendar-store-request.ts:9](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/calendar-store-request.ts#L9)

Coerce a request body's `events` field into stored event documents, fixing up
date fields that crossed the wire as strings. Anything else becomes empty.

## Parameters

### events

`unknown`

## Returns

[`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]
