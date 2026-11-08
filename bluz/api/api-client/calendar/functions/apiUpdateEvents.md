[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar](../index.md) / apiUpdateEvents

# Function: apiUpdateEvents()

> **apiUpdateEvents**(`events`, `initiator?`, `props?`, `iterationId?`): `Promise`\<[`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]\>

Defined in: [ui/src/api-client/calendar.ts:235](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-client/calendar.ts#L235)

Updates many existing events in one request (`PATCH /api/event`).

## Parameters

### events

[`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]

### initiator?

[`EventChangeInitiator`](../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md)

### props?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

### iterationId?

`string`

## Returns

`Promise`\<[`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]\>
