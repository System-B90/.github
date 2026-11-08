[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / setHiveCache

# Variable: setHiveCache

> `const` **setHiveCache**: (`id`, `hiveCache`) => `Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md)\> = `setIterationHiveCache`

Defined in: [ui/src/api-server/db-iterations.ts:459](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/db-iterations.ts#L459)

Overwrite an iteration's Hive name cache, e.g. after a manual "sync Hive
info" request (#379).

## Parameters

### id

`string`

### hiveCache

[`HiveIterationCache`](../../../../../api-shared/types/iteration/type-aliases/HiveIterationCache.md)

## Returns

`Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md)\>
