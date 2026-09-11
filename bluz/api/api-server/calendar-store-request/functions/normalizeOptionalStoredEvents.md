[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/calendar-store-request](../index.md) / normalizeOptionalStoredEvents

# Function: normalizeOptionalStoredEvents()

> **normalizeOptionalStoredEvents**(`events`): [`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)[] \| `undefined`

Defined in: [ui/src/api-server/calendar-store-request.ts:23](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/calendar-store-request.ts#L23)

Same coercion for PATCH-style bodies where `events` is optional: an absent
key means "keep whatever is stored" and must be distinguishable from an
explicit empty list (#512). A present-but-wrong-typed value is a client
error, not silently an empty draft.

## Parameters

### events

`unknown`

## Returns

[`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)[] \| `undefined`
