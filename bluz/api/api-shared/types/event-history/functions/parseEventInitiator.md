[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event-history](../index.md) / parseEventInitiator

# Function: parseEventInitiator()

> **parseEventInitiator**(`value`): [`EventChangeInitiator`](../enumerations/EventChangeInitiator.md)

Defined in: [ui/src/api-shared/types/event-history.ts:72](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/types/event-history.ts#L72)

Narrow an untrusted header value to a known initiator.

## Parameters

### value

`string` \| `null` \| `undefined`

Raw header value, possibly null.

## Returns

[`EventChangeInitiator`](../enumerations/EventChangeInitiator.md)

The matching initiator, or [EventChangeInitiator.Unknown](../enumerations/EventChangeInitiator.md#unknown).
