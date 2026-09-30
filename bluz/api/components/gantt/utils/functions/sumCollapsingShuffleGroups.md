[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / sumCollapsingShuffleGroups

# Function: sumCollapsingShuffleGroups()

> **sumCollapsingShuffleGroups**(`entries`, `state`): `number`

Defined in: [ui/src/components/gantt/utils.tsx:136](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/utils.tsx#L136)

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
