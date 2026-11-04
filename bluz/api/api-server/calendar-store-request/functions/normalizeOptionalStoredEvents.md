[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/calendar-store-request](../index.md) / normalizeOptionalStoredEvents

# Function: normalizeOptionalStoredEvents()

> **normalizeOptionalStoredEvents**(`events`): [`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)[] \| `undefined`

Defined in: [ui/src/api-server/calendar-store-request.ts:44](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/calendar-store-request.ts#L44)

Same coercion for PATCH-style bodies where `events` is optional: an absent
key means "keep whatever is stored" and must be distinguishable from an
explicit empty list (#512). A present-but-wrong-typed value is a client
error, not silently an empty draft.

## Parameters

### events

`unknown`

## Returns

[`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)[] \| `undefined`
