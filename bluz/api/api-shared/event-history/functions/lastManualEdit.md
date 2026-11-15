[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/event-history](../index.md) / lastManualEdit

# Function: lastManualEdit()

> **lastManualEdit**\<`T`\>(`entries`): `T` \| `null`

Defined in: [ui/src/api-shared/event-history.ts:105](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-shared/event-history.ts#L105)

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
