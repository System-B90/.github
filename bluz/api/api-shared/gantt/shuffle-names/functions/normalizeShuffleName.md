[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / normalizeShuffleName

# Function: normalizeShuffleName()

> **normalizeShuffleName**(`name`): `string`

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:6](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/gantt/shuffle-names.ts#L6)

The canonical form of a shuffle name: trimmed, with inner runs of whitespace
collapsed. Tags are matched by exact string, so "א  ב" and "א ב" would
otherwise be two shuffles that look identical in every chip and dropdown.

## Parameters

### name

`string`

## Returns

`string`
