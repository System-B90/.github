[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-breaks](../index.md) / breakKindForBoundary

# Function: breakKindForBoundary()

> **breakKindForBoundary**(`before`, `after`, `exerciseRunMinutes`, `classRunMinutes`): `"post-long-exercise"` \| `"between-syllabuses"` \| `"prayer-cover"` \| `"post-lecture"` \| `"room-change"` \| `null`

Defined in: [ui/src/api-shared/gantt/cut-breaks.ts:126](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-breaks.ts#L126)

The kind of break, if any, that the boundary between `before` and `after`
earns. Returns the highest-priority kind that applies — one boundary never
grows two stacked breaks.

`exerciseRunMinutes` is the length of the continuous same-type run ending at
`before`, which is what the 90-minute ע"ע rule measures. `classRunMinutes`
is the length of the continuous run of *any* lecture/ע"ע mix ending at
`before` — arbitrary consecutive lecture/ע"ע events accumulate together,
which is what the 45-minute post-lecture rule measures.

## Parameters

### before

[`PlacedItem`](../type-aliases/PlacedItem.md)

### after

[`PlacedItem`](../type-aliases/PlacedItem.md)

### exerciseRunMinutes

`number`

### classRunMinutes

`number`

## Returns

`"post-long-exercise"` \| `"between-syllabuses"` \| `"prayer-cover"` \| `"post-lecture"` \| `"room-change"` \| `null`
