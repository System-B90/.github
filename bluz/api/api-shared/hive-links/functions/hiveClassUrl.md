[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/hive-links](../index.md) / hiveClassUrl

# Function: hiveClassUrl()

> **hiveClassUrl**(`hiveClassId`, `baseUrl?`): `string` \| `null`

Defined in: [ui/src/api-shared/hive-links.ts:68](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/hive-links.ts#L68)

Link to a student group in Hive's mentor view — where its current lesson
and queue are shown and can be reassigned by hand.

## Parameters

### hiveClassId

`number` \| `null` \| `undefined`

Hive class (student group) id.

### baseUrl?

`string`

Hive instance; defaults to `NEXT_PUBLIC_HIVE_URL`.

## Returns

`string` \| `null`

The absolute URL, or null when the id or Hive URL is missing.
