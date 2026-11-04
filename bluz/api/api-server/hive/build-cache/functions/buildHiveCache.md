[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/build-cache](../index.md) / buildHiveCache

# Function: buildHiveCache()

> **buildHiveCache**(`hiveUrl?`): `Promise`\<[`HiveIterationCache`](../../../../api-shared/types/iteration/type-aliases/HiveIterationCache.md) \| `undefined`\>

Defined in: [ui/src/api-server/hive/build-cache.ts:15](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/hive/build-cache.ts#L15)

Snapshot the Hive module / subject / room names for a Hive instance. Hive
ids are not stable across iterations, so we freeze the names by id.
Best-effort: a Hive failure must not block the caller.

## Parameters

### hiveUrl?

`string`

## Returns

`Promise`\<[`HiveIterationCache`](../../../../api-shared/types/iteration/type-aliases/HiveIterationCache.md) \| `undefined`\>
