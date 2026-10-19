[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/calendar-store-request](../index.md) / parseDraftRange

# Function: parseDraftRange()

> **parseDraftRange**(`value`): [`CalendarDraftRange`](../../../api-shared/types/type-aliases/CalendarDraftRange.md) \| `undefined`

Defined in: [ui/src/api-server/calendar-store-request.ts:49](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/calendar-store-request.ts#L49)

A validated range, or `undefined` when none was sent. Both ends are
required together and must be real instants in order.

## Parameters

### value

`Partial`\<[`CalendarDraftRange`](../../../api-shared/types/type-aliases/CalendarDraftRange.md)\>

## Returns

[`CalendarDraftRange`](../../../api-shared/types/type-aliases/CalendarDraftRange.md) \| `undefined`
