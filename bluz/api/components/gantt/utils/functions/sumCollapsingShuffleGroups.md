[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / sumCollapsingShuffleGroups

# Function: sumCollapsingShuffleGroups()

> **sumCollapsingShuffleGroups**(`entries`, `state`): `number`

Defined in: [ui/src/components/gantt/utils.tsx:136](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/utils.tsx#L136)

Sums per-event minutes the way module/syllabus totals do: events sharing a
shuffle group count once, at their longest member, since the group is one
lesson repeated per shuffle rather than several lessons (#699).

## Parameters

### entries

`Iterable`\<\{ `eventId`: `string`; `minutes`: `number`; \}\>

### state

[`NormalizedStore`](../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

## Returns

`number`
