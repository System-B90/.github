[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/hive-links](../index.md) / hiveClassUrl

# Function: hiveClassUrl()

> **hiveClassUrl**(`hiveClassId`, `baseUrl?`): `string` \| `null`

Defined in: [ui/src/api-shared/hive-links.ts:70](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/hive-links.ts#L70)

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
