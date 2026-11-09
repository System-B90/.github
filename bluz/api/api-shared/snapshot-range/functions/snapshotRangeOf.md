[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/snapshot-range](../index.md) / snapshotRangeOf

# Function: snapshotRangeOf()

> **snapshotRangeOf**(`snapshot`, `events`): \{ `rangeEnd`: `Date`; `rangeStart`: `Date`; \} \| `undefined`

Defined in: [ui/src/api-shared/snapshot-range.ts:34](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/snapshot-range.ts#L34)

The range a snapshot covers: the one stored at capture time, else (for
snapshots taken before ranges were stored) the span of its own events.
`undefined` for an empty legacy snapshot, which covers nothing.

## Parameters

### snapshot

`Partial`\<[`CalendarDraftRange`](../../types/type-aliases/CalendarDraftRange.md)\>

### events

readonly `Timed`[]

## Returns

\{ `rangeEnd`: `Date`; `rangeStart`: `Date`; \} \| `undefined`
