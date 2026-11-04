[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/hive-links](../index.md) / hiveSubjectUrl

# Function: hiveSubjectUrl()

> **hiveSubjectUrl**(`subjectId`, `baseUrl?`): `string` \| `null`

Defined in: [ui/src/api-shared/hive-links.ts:52](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/hive-links.ts#L52)

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
