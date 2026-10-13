[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar](../index.md) / apiDeleteEvents

# Function: apiDeleteEvents()

> **apiDeleteEvents**(`eventIds`, `initiator?`, `props?`, `iterationId?`): `Promise`\<`void`\>

Defined in: [ui/src/api-client/calendar.ts:262](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-client/calendar.ts#L262)

Deletes many events in one request (`DELETE /api/event/bulk`).

## Parameters

### eventIds

`string`[]

### initiator?

[`EventChangeInitiator`](../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md)

### props?

[`ClientApiProps`](../../common/type-aliases/ClientApiProps.md)

### iterationId?

`string`

## Returns

`Promise`\<`void`\>
