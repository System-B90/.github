[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / pushAllEvents

# Function: pushAllEvents()

> **pushAllEvents**(`userId`, `events`, `iterationId?`): `Promise`\<`number`\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:740](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/google/google-calendar-service.ts#L740)

Pushes a full batch of the user's events (used by the manual "sync now"
action to backfill everything at once).

## Parameters

### userId

`string`

### events

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

### iterationId?

`string`

## Returns

`Promise`\<`number`\>
