[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/hive-links](../index.md) / hiveSubjectUrl

# Function: hiveSubjectUrl()

> **hiveSubjectUrl**(`subjectId`, `baseUrl?`): `string` \| `null`

Defined in: [ui/src/api-shared/hive-links.ts:52](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-shared/hive-links.ts#L52)

Link to a subject's Hive page.

## Parameters

### subjectId

`number` \| `null` \| `undefined`

Hive subject id.

### baseUrl?

`string`

Hive instance; defaults to `NEXT_PUBLIC_HIVE_URL`.

## Returns

`string` \| `null`

The absolute URL, or null when the id or Hive URL is missing.
