[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / normalizeShuffleName

# Function: normalizeShuffleName()

> **normalizeShuffleName**(`name`): `string`

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:14](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/shuffle-names.ts#L14)

The canonical form of a shuffle name: trimmed, with inner runs of whitespace
collapsed. Tags are matched by exact string, so "א  ב" and "א ב" would
otherwise be two shuffles that look identical in every chip and dropdown.

## Parameters

### name

`string`

## Returns

`string`
