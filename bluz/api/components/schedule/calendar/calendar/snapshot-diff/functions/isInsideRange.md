[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/snapshot-diff](../index.md) / isInsideRange

# Function: isInsideRange()

> **isInsideRange**(`event`, `range`): `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar/snapshot-diff.ts:56](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/components/schedule/calendar/calendar/snapshot-diff.ts#L56)

Whether `event` lies wholly inside `range` — the same rule the server uses
to pick the live events a restore replaces, so an event straddling an edge
is never offered for removal.

## Parameters

### event

`Pick`\<[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md), `"endTime"` \| `"startTime"`\>

### range

`Range`

## Returns

`boolean`
