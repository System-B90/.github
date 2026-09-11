[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/iteration](../index.md) / HiveCacheChanges

# Type Alias: HiveCacheChanges

> **HiveCacheChanges** = `object`

Defined in: [ui/src/api-shared/types/iteration.ts:39](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L39)

How a manual "sync Hive info" (#379) changed the cached names. Counts are
summed across modules, subjects and rooms.

## Properties

### added

> **added**: `number`

Defined in: [ui/src/api-shared/types/iteration.ts:41](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L41)

Ids present in Hive that the cache did not have.

***

### removed

> **removed**: `number`

Defined in: [ui/src/api-shared/types/iteration.ts:45](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L45)

Cached ids that Hive no longer returns.

***

### unchanged

> **unchanged**: `number`

Defined in: [ui/src/api-shared/types/iteration.ts:47](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L47)

Ids whose cached name already matched.

***

### updated

> **updated**: `number`

Defined in: [ui/src/api-shared/types/iteration.ts:43](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L43)

Ids whose cached name differs from Hive's.
