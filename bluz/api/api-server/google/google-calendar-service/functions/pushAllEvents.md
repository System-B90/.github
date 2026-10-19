[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / pushAllEvents

# Function: pushAllEvents()

> **pushAllEvents**(`userId`, `events`, `iterationId?`): `Promise`\<`number`\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:740](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/google/google-calendar-service.ts#L740)

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
