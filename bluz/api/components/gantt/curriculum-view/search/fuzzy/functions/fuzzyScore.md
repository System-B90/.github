[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/curriculum-view/search/fuzzy](../index.md) / fuzzyScore

# Function: fuzzyScore()

> **fuzzyScore**(`query`, `target`): `number`

Defined in: [ui/src/components/gantt/curriculum-view/search/fuzzy.ts:25](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/search/fuzzy.ts#L25)

Score how well `query` matches `target`.

- `0` means no match (not every query character is present, in order).
- Higher is better: exact substrings beat scattered subsequences, earlier
  matches beat later ones, and consecutive runs are rewarded.

## Parameters

### query

`string`

### target

`string`

## Returns

`number`
