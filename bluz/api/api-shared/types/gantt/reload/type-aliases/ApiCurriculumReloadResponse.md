[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / ApiCurriculumReloadResponse

# Type Alias: ApiCurriculumReloadResponse

> **ApiCurriculumReloadResponse** = `object`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:98](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L98)

## Properties

### addedEvents

> **addedEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:103](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L103)

Counts of what was actually written (all zero on a dry run).

***

### applied

> **applied**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:100](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L100)

False for a dry run — the diff is a proposal, nothing was written.

***

### createdCourses

> **createdCourses**: `object`[]

Defined in: [ui/src/api-shared/types/gantt/reload.ts:109](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L109)

Courses newly created for shuffles introduced since the cut.

#### id

> **id**: `string`

#### name

> **name**: `string`

***

### diff

> **diff**: [`ReloadDiff`](ReloadDiff.md)

Defined in: [ui/src/api-shared/types/gantt/reload.ts:101](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L101)

***

### hiveSubjectsUnavailable

> **hiveSubjectsUnavailable**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:115](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L115)

True when Hive could not supply the module → subject map for this run and
events were left without their subject (and color) as a result (#662).
A later reload, once Hive is reachable, repairs them.

***

### removedEvents

> **removedEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:105](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L105)

***

### skippedConflicts

> **skippedConflicts**: `number`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:107](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L107)

Conflicts left untouched because the user did not override them.

***

### updatedEvents

> **updatedEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:104](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L104)
