[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event-history](../index.md) / parseEventInitiator

# Function: parseEventInitiator()

> **parseEventInitiator**(`value`): [`EventChangeInitiator`](../enumerations/EventChangeInitiator.md)

Defined in: [ui/src/api-shared/types/event-history.ts:76](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types/event-history.ts#L76)

Narrow an untrusted header value to a known initiator.

## Parameters

### value

`string` \| `null` \| `undefined`

Raw header value, possibly null.

## Returns

[`EventChangeInitiator`](../enumerations/EventChangeInitiator.md)

The matching initiator, or [EventChangeInitiator.Unknown](../enumerations/EventChangeInitiator.md#unknown).
