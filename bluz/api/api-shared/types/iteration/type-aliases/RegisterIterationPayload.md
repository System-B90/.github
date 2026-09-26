[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/iteration](../index.md) / RegisterIterationPayload

# Type Alias: RegisterIterationPayload

> **RegisterIterationPayload** = `object`

Defined in: [ui/src/api-shared/types/iteration.ts:96](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L96)

Payload to register a new iteration. `dbName` is derived from `id` when omitted.

## Properties

### dbName?

> `optional` **dbName?**: `string`

Defined in: [ui/src/api-shared/types/iteration.ts:99](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L99)

***

### endDate?

> `optional` **endDate?**: `Date` \| `null` \| `string`

Defined in: [ui/src/api-shared/types/iteration.ts:104](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L104)

***

### ganttCurriculumId?

> `optional` **ganttCurriculumId?**: `string`

Defined in: [ui/src/api-shared/types/iteration.ts:105](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L105)

***

### hiveCache?

> `optional` **hiveCache?**: [`HiveIterationCache`](HiveIterationCache.md)

Defined in: [ui/src/api-shared/types/iteration.ts:102](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L102)

Optional pre-computed Hive name cache (the route fills this in).

***

### hiveUrl?

> `optional` **hiveUrl?**: `string`

Defined in: [ui/src/api-shared/types/iteration.ts:100](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L100)

***

### id

> **id**: [`IterationId`](IterationId.md)

Defined in: [ui/src/api-shared/types/iteration.ts:97](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L97)

***

### label

> **label**: `string`

Defined in: [ui/src/api-shared/types/iteration.ts:98](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L98)

***

### startDate?

> `optional` **startDate?**: `Date` \| `string`

Defined in: [ui/src/api-shared/types/iteration.ts:103](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L103)
