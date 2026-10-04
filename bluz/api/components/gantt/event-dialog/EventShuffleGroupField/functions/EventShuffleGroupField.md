[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/event-dialog/EventShuffleGroupField](../index.md) / EventShuffleGroupField

# Function: EventShuffleGroupField()

> **EventShuffleGroupField**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/event-dialog/EventShuffleGroupField.tsx:94](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/event-dialog/EventShuffleGroupField.tsx#L94)

Splits one event into a shuffle group: one event per selected shuffle, all
carrying the same name, so each shuffle can hold the lesson at its own time
(#699).

The copies are separate rows on purpose — each keeps its own placement, cut
and Hive linkage — and the group only changes how they are counted: the
shuffles run in parallel, so time is never the sum of all members. Shuffles
may differ within a module; only the syllabus total must match.

## Parameters

### \_\_namedParameters

#### event

[`GanttEvent`](../../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)

#### eventId

`string`

#### moduleId

`string`

#### shuffleDescriptions?

[`ShuffleDescriptions`](../../../../../api-shared/gantt/shuffle-names/type-aliases/ShuffleDescriptions.md) = `{}`

The syllabus' shuffle name → description map.

#### shuffleOptions

`string`[]

Shuffle names defined on the parent syllabus.

#### syllabusId

`string` \| `null`

## Returns

`Element`
