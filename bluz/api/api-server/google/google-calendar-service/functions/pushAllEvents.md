[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / pushAllEvents

# Function: pushAllEvents()

> **pushAllEvents**(`userId`, `events`, `iterationId?`): `Promise`\<`number`\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:819](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/google/google-calendar-service.ts#L819)

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
