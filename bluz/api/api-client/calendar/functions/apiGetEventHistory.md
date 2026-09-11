[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar](../index.md) / apiGetEventHistory

# Function: apiGetEventHistory()

> **apiGetEventHistory**(`eventId`, `iterationId?`): `Promise`\<[`ApiEventHistoryResponse`](../../../api-shared/types/event-history/type-aliases/ApiEventHistoryResponse.md)\>

Defined in: [ui/src/api-client/calendar.ts:154](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/calendar.ts#L154)

Fetch one event's change log ("היסטוריית שינויים"), newest first.

## Parameters

### eventId

`string`

Event whose log is requested.

### iterationId?

`string`

Iteration to read from; defaults to the current run.

## Returns

`Promise`\<[`ApiEventHistoryResponse`](../../../api-shared/types/event-history/type-aliases/ApiEventHistoryResponse.md)\>
