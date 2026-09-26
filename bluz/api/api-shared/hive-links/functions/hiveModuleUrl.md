[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/hive-links](../index.md) / hiveModuleUrl

# Function: hiveModuleUrl()

> **hiveModuleUrl**(`subjectId`, `moduleId`, `baseUrl?`): `string` \| `null`

Defined in: [ui/src/api-shared/hive-links.ts:34](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/hive-links.ts#L34)

Link to a module's Hive page — the one screen that lists both its lessons
(with their group→queue rules) and its queues. Hive has no per-lesson
route, so this is as deep as a lesson link goes.

## Parameters

### subjectId

`number` \| `null` \| `undefined`

Hive subject id.

### moduleId

`number` \| `null` \| `undefined`

Hive module id.

### baseUrl?

`string`

Hive instance; defaults to `NEXT_PUBLIC_HIVE_URL`.

## Returns

`string` \| `null`

The absolute URL, or null when ids or the Hive URL are missing.

## Example

```typescript
hiveModuleUrl(4, 17); // "https://hive.example/course/4/17"
```
