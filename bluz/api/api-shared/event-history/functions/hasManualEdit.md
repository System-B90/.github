[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/event-history](../index.md) / hasManualEdit

# Function: hasManualEdit()

> **hasManualEdit**(`entries`): `boolean`

Defined in: [ui/src/api-shared/event-history.ts:92](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-shared/event-history.ts#L92)

Whether an event's log contains a human edit, i.e. any change whose
initiator is not part of the gantt pipeline.

## Parameters

### entries

`Pick`\<[`EventHistoryEntry`](../../types/event-history/type-aliases/EventHistoryEntry.md), `"initiator"`\>[]

The event's history rows (any order).

## Returns

`boolean`
