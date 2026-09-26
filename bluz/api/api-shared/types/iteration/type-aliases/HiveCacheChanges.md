[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/iteration](../index.md) / HiveCacheChanges

# Type Alias: HiveCacheChanges

> **HiveCacheChanges** = `object`

Defined in: [ui/src/api-shared/types/iteration.ts:39](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L39)

How a manual "sync Hive info" (#379) changed the cached names. Counts are
summed across modules, subjects and rooms.

## Properties

### added

> **added**: `number`

Defined in: [ui/src/api-shared/types/iteration.ts:41](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L41)

Ids present in Hive that the cache did not have.

***

### removed

> **removed**: `number`

Defined in: [ui/src/api-shared/types/iteration.ts:45](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L45)

Cached ids that Hive no longer returns.

***

### unchanged

> **unchanged**: `number`

Defined in: [ui/src/api-shared/types/iteration.ts:47](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L47)

Ids whose cached name already matched.

***

### updated

> **updated**: `number`

Defined in: [ui/src/api-shared/types/iteration.ts:43](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L43)

Ids whose cached name differs from Hive's.
