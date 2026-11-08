[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar](../index.md) / apiDeleteEvents

# Function: apiDeleteEvents()

> **apiDeleteEvents**(`eventIds`, `initiator?`, `props?`, `iterationId?`): `Promise`\<`void`\>

Defined in: [ui/src/api-client/calendar.ts:273](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-client/calendar.ts#L273)

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
