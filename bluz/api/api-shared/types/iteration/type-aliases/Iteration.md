[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/iteration](../index.md) / Iteration

# Type Alias: Iteration

> **Iteration** = `object`

Defined in: [ui/src/api-shared/types/iteration.ts:61](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L61)

A single course iteration (bi-annual run). The set of all iterations is
stored in the shared `bluz_meta` DB; the calendar data for each iteration
lives in the database named by `dbName`.

## Properties

### createdAt

> **createdAt**: `Date` \| `string`

Defined in: [ui/src/api-shared/types/iteration.ts:78](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L78)

***

### dbName

> **dbName**: `string`

Defined in: [ui/src/api-shared/types/iteration.ts:67](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L67)

Mongo DB backing this iteration ("bluz", "bluz_2026b", ...).

***

### endDate

> **endDate**: `Date` \| `null` \| `string`

Defined in: [ui/src/api-shared/types/iteration.ts:73](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L73)

***

### ganttCurriculumId?

> `optional` **ganttCurriculumId?**: `string`

Defined in: [ui/src/api-shared/types/iteration.ts:77](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L77)

Optional link to the Postgres curriculum that drove this iteration.

***

### hiveCache?

> `optional` **hiveCache?**: [`HiveIterationCache`](HiveIterationCache.md)

Defined in: [ui/src/api-shared/types/iteration.ts:71](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L71)

Cached Hive names, snapshotted at creation time.

***

### hiveUrl?

> `optional` **hiveUrl?**: `string`

Defined in: [ui/src/api-shared/types/iteration.ts:69](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L69)

Per-iteration Hive instance base URL (the Hive instance changes each run).

***

### id

> **id**: [`IterationId`](IterationId.md)

Defined in: [ui/src/api-shared/types/iteration.ts:63](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L63)

Stable id, e.g. "2026a".

***

### isCurrent

> **isCurrent**: `boolean`

Defined in: [ui/src/api-shared/types/iteration.ts:75](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L75)

Exactly one iteration is current → the writable / active run.

***

### label

> **label**: `string`

Defined in: [ui/src/api-shared/types/iteration.ts:65](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L65)

Human label, e.g. "מחזור 2026 א'".

***

### startDate

> **startDate**: `Date` \| `string`

Defined in: [ui/src/api-shared/types/iteration.ts:72](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L72)

***

### updatedAt

> **updatedAt**: `Date` \| `string`

Defined in: [ui/src/api-shared/types/iteration.ts:79](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/iteration.ts#L79)
