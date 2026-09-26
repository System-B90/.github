[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/event-history](../index.md) / lastManualEdit

# Function: lastManualEdit()

> **lastManualEdit**\<`T`\>(`entries`): `T` \| `null`

Defined in: [ui/src/api-shared/event-history.ts:99](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/event-history.ts#L99)

The most recent manual change of an event, used to explain a skipped reload
in the conflicts dialog.

## Type Parameters

### T

`T` *extends* `Pick`\<[`EventHistoryEntry`](../../types/event-history/type-aliases/EventHistoryEntry.md), `"changedAt"` \| `"initiator"`\>

## Parameters

### entries

`T`[]

The event's history rows (any order).

## Returns

`T` \| `null`

The newest non-gantt row, or null when the event was never edited.
