[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/schedule-feed](../index.md) / normalizeCategoryName

# Function: normalizeCategoryName()

> **normalizeCategoryName**(`name`): `string`

Defined in: [ui/src/api-server/hive/schedule-feed.ts:151](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/hive/schedule-feed.ts#L151)

Hebrew abbreviation marks dropped, so Bluz's `ע"ע` meets Hive's stock
`עע` category.

## Parameters

### name

`string`

A category or event-type name.

## Returns

`string`

The name compared across the two systems.
