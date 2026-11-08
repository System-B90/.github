[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / ApiCurriculumReloadResponse

# Type Alias: ApiCurriculumReloadResponse

> **ApiCurriculumReloadResponse** = `object`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:108](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/gantt/reload.ts#L108)

## Properties

### addedEvents

> **addedEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:113](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/gantt/reload.ts#L113)

Counts of what was actually written (all zero on a dry run).

***

### applied

> **applied**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:110](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/gantt/reload.ts#L110)

False for a dry run — the diff is a proposal, nothing was written.

***

### createdCourses

> **createdCourses**: `object`[]

Defined in: [ui/src/api-shared/types/gantt/reload.ts:119](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/gantt/reload.ts#L119)

Courses newly created for shuffles introduced since the cut.

#### id

> **id**: `string`

#### name

> **name**: `string`

***

### diff

> **diff**: [`ReloadDiff`](ReloadDiff.md)

Defined in: [ui/src/api-shared/types/gantt/reload.ts:111](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/gantt/reload.ts#L111)

***

### hiveSubjectsUnavailable

> **hiveSubjectsUnavailable**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:125](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/gantt/reload.ts#L125)

True when Hive could not supply the module → subject map for this run and
events were left without their subject (and color) as a result (#662).
A later reload, once Hive is reachable, repairs them.

***

### removedEvents

> **removedEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:115](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/gantt/reload.ts#L115)

***

### skippedConflicts

> **skippedConflicts**: `number`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:117](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/gantt/reload.ts#L117)

Conflicts left untouched because the user did not override them.

***

### updatedEvents

> **updatedEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:114](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/gantt/reload.ts#L114)
