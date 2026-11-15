[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar](../index.md) / apiUpdateEvents

# Function: apiUpdateEvents()

> **apiUpdateEvents**(`events`, `initiator?`, `props?`, `iterationId?`): `Promise`\<[`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]\>

Defined in: [ui/src/api-client/calendar.ts:235](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-client/calendar.ts#L235)

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
