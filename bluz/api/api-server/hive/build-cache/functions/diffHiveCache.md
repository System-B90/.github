[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/build-cache](../index.md) / diffHiveCache

# Function: diffHiveCache()

> **diffHiveCache**(`before`, `after`): [`HiveCacheChanges`](../../../../api-shared/types/iteration/type-aliases/HiveCacheChanges.md)

Defined in: [ui/src/api-server/hive/build-cache.ts:51](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/hive/build-cache.ts#L51)

Summarise what a fresh snapshot changes relative to the stored one, so a
manual sync (#379) can report a result instead of succeeding silently. The
cache is derived data — never user-edited — so the sync itself is a plain
overwrite and this is a report, not a conflict resolution.

## Parameters

### before

[`HiveIterationCache`](../../../../api-shared/types/iteration/type-aliases/HiveIterationCache.md) \| `undefined`

### after

[`HiveIterationCache`](../../../../api-shared/types/iteration/type-aliases/HiveIterationCache.md)

## Returns

[`HiveCacheChanges`](../../../../api-shared/types/iteration/type-aliases/HiveCacheChanges.md)
