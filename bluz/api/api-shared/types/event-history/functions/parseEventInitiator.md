[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event-history](../index.md) / parseEventInitiator

# Function: parseEventInitiator()

> **parseEventInitiator**(`value`): [`EventChangeInitiator`](../enumerations/EventChangeInitiator.md)

Defined in: [ui/src/api-shared/types/event-history.ts:76](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/event-history.ts#L76)

Narrow an untrusted header value to a known initiator.

## Parameters

### value

`string` \| `null` \| `undefined`

Raw header value, possibly null.

## Returns

[`EventChangeInitiator`](../enumerations/EventChangeInitiator.md)

The matching initiator, or [EventChangeInitiator.Unknown](../enumerations/EventChangeInitiator.md#unknown).
