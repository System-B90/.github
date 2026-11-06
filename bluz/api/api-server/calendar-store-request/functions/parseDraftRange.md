[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/calendar-store-request](../index.md) / parseDraftRange

# Function: parseDraftRange()

> **parseDraftRange**(`value`, `what?`): [`CalendarDraftRange`](../../../api-shared/types/type-aliases/CalendarDraftRange.md) \| `undefined`

Defined in: [ui/src/api-server/calendar-store-request.ts:74](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/calendar-store-request.ts#L74)

A validated range, or `undefined` when none was sent. Both ends are
required together and must be real instants in order.

## Parameters

### value

`Partial`\<[`CalendarDraftRange`](../../../api-shared/types/type-aliases/CalendarDraftRange.md)\>

### what?

`string` = `"Draft"`

## Returns

[`CalendarDraftRange`](../../../api-shared/types/type-aliases/CalendarDraftRange.md) \| `undefined`
