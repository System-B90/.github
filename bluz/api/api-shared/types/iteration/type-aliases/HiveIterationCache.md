[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/iteration](../index.md) / HiveIterationCache

# Type Alias: HiveIterationCache

> **HiveIterationCache** = `object`

Defined in: [ui/src/api-shared/types/iteration.ts:24](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L24)

Snapshot of Hive names taken when an iteration is created. The Hive instance
changes every iteration, so numeric Hive ids are not stable across runs — we
cache the human names by id so a past iteration can be displayed even after
its Hive instance is gone or its ids have been reused.

## Properties

### cachedAt

> **cachedAt**: `string`

Defined in: [ui/src/api-shared/types/iteration.ts:32](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L32)

When this snapshot was taken (ISO string).

***

### modules

> **modules**: `Record`\<`string`, `string`\>

Defined in: [ui/src/api-shared/types/iteration.ts:26](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L26)

Hive module id → module name.

***

### rooms

> **rooms**: `Record`\<`string`, `string`\>

Defined in: [ui/src/api-shared/types/iteration.ts:30](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L30)

Hive room id → room name.

***

### subjects

> **subjects**: `Record`\<`string`, `string`\>

Defined in: [ui/src/api-shared/types/iteration.ts:28](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L28)

Hive subject id → subject display name.
