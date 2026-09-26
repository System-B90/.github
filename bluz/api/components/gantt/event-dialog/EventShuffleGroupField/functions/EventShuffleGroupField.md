[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/event-dialog/EventShuffleGroupField](../index.md) / EventShuffleGroupField

# Function: EventShuffleGroupField()

> **EventShuffleGroupField**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/event-dialog/EventShuffleGroupField.tsx:90](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/event-dialog/EventShuffleGroupField.tsx#L90)

Splits one event into a shuffle group: one event per selected shuffle, all
carrying the same name, so each shuffle can hold the lesson at its own time
(#699).

The copies are separate rows on purpose — each keeps its own placement, cut
and Hive linkage — and the group only changes how they are counted: a
module's required time takes the longest member, not the sum of all of them.

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
