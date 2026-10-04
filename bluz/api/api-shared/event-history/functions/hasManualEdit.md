[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/event-history](../index.md) / hasManualEdit

# Function: hasManualEdit()

> **hasManualEdit**(`entries`): `boolean`

Defined in: [ui/src/api-shared/event-history.ts:87](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/event-history.ts#L87)

Whether an event's log contains a human edit, i.e. any change whose
initiator is not part of the gantt pipeline.

## Parameters

### entries

`Pick`\<[`EventHistoryEntry`](../../types/event-history/type-aliases/EventHistoryEntry.md), `"initiator"`\>[]

The event's history rows (any order).

## Returns

`boolean`
