[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/curriculum-view/search/fuzzy](../index.md) / fuzzyScore

# Function: fuzzyScore()

> **fuzzyScore**(`query`, `target`): `number`

Defined in: [ui/src/components/gantt/curriculum-view/search/fuzzy.ts:26](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/components/gantt/curriculum-view/search/fuzzy.ts#L26)

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
