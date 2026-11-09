[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/curriculum-view/search/fuzzy](../index.md) / fuzzyScore

# Function: fuzzyScore()

> **fuzzyScore**(`query`, `target`): `number`

Defined in: [ui/src/components/gantt/curriculum-view/search/fuzzy.ts:26](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/gantt/curriculum-view/search/fuzzy.ts#L26)

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
