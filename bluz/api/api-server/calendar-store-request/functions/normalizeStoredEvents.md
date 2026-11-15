[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/calendar-store-request](../index.md) / normalizeStoredEvents

# Function: normalizeStoredEvents()

> **normalizeStoredEvents**(`events`): [`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

Defined in: [ui/src/api-server/calendar-store-request.ts:10](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/calendar-store-request.ts#L10)

Coerce a request body's `events` field into stored event documents, fixing up
date fields that crossed the wire as strings. Anything else becomes empty.

## Parameters

### events

`unknown`

## Returns

[`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]
