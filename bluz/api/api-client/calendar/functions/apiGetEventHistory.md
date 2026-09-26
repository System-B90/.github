[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar](../index.md) / apiGetEventHistory

# Function: apiGetEventHistory()

> **apiGetEventHistory**(`eventId`, `iterationId?`): `Promise`\<[`ApiEventHistoryResponse`](../../../api-shared/types/event-history/type-aliases/ApiEventHistoryResponse.md)\>

Defined in: [ui/src/api-client/calendar.ts:174](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/calendar.ts#L174)

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
