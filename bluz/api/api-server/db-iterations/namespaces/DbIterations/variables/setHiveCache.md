[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / setHiveCache

# Variable: setHiveCache

> `const` **setHiveCache**: (`id`, `hiveCache`) => `Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md)\> = `setIterationHiveCache`

Defined in: [ui/src/api-server/db-iterations.ts:384](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/db-iterations.ts#L384)

Overwrite an iteration's Hive name cache, e.g. after a manual "sync Hive
info" request (#379).

## Parameters

### id

`string`

### hiveCache

[`HiveIterationCache`](../../../../../api-shared/types/iteration/type-aliases/HiveIterationCache.md)

## Returns

`Promise`\<[`Iteration`](../../../../../api-shared/types/iteration/type-aliases/Iteration.md)\>
