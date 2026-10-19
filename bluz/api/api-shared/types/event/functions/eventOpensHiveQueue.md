[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventOpensHiveQueue

# Function: eventOpensHiveQueue()

> **eventOpensHiveQueue**(`event`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:159](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/event.ts#L159)

True when an event opens a Hive queue for at least one shuffle — the gate
for both the lesson sync and the go-live activator.

## Parameters

### event

`Pick`\<[`Event`](../type-aliases/Event.md), `"courses"` \| `"hiveModule"` \| `"hiveQueues"`\>

The event to inspect.

## Returns

`boolean`

Whether the event has a usable queue mapping.
