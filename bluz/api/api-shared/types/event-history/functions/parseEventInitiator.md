[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event-history](../index.md) / parseEventInitiator

# Function: parseEventInitiator()

> **parseEventInitiator**(`value`): [`EventChangeInitiator`](../enumerations/EventChangeInitiator.md)

Defined in: [ui/src/api-shared/types/event-history.ts:76](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/types/event-history.ts#L76)

Narrow an untrusted header value to a known initiator.

## Parameters

### value

`string` \| `null` \| `undefined`

Raw header value, possibly null.

## Returns

[`EventChangeInitiator`](../enumerations/EventChangeInitiator.md)

The matching initiator, or [EventChangeInitiator.Unknown](../enumerations/EventChangeInitiator.md#unknown).
