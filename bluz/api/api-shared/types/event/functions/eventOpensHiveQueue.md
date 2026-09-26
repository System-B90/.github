[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventOpensHiveQueue

# Function: eventOpensHiveQueue()

> **eventOpensHiveQueue**(`event`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:135](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/event.ts#L135)

True when an event opens a Hive queue for at least one shuffle — the gate
for both the lesson sync and the go-live activator.

## Parameters

### event

`Pick`\<[`Event`](../type-aliases/Event.md), `"courses"` \| `"hiveModule"` \| `"hiveQueues"`\>

The event to inspect.

## Returns

`boolean`

Whether the event has a usable queue mapping.
