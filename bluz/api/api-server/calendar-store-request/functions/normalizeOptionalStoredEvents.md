[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/calendar-store-request](../index.md) / normalizeOptionalStoredEvents

# Function: normalizeOptionalStoredEvents()

> **normalizeOptionalStoredEvents**(`events`): [`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)[] \| `undefined`

Defined in: [ui/src/api-server/calendar-store-request.ts:44](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/calendar-store-request.ts#L44)

Same coercion for PATCH-style bodies where `events` is optional: an absent
key means "keep whatever is stored" and must be distinguishable from an
explicit empty list (#512). A present-but-wrong-typed value is a client
error, not silently an empty draft.

## Parameters

### events

`unknown`

## Returns

[`DbEventDocument`](../../../api-shared/types/event/type-aliases/DbEventDocument.md)[] \| `undefined`
