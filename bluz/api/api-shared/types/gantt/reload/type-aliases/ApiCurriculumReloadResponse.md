[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / ApiCurriculumReloadResponse

# Type Alias: ApiCurriculumReloadResponse

> **ApiCurriculumReloadResponse** = `object`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:91](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/reload.ts#L91)

## Properties

### addedEvents

> **addedEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:96](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/reload.ts#L96)

Counts of what was actually written (all zero on a dry run).

***

### applied

> **applied**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:93](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/reload.ts#L93)

False for a dry run — the diff is a proposal, nothing was written.

***

### createdCourses

> **createdCourses**: `object`[]

Defined in: [ui/src/api-shared/types/gantt/reload.ts:102](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/reload.ts#L102)

Courses newly created for shuffles introduced since the cut.

#### id

> **id**: `string`

#### name

> **name**: `string`

***

### diff

> **diff**: [`ReloadDiff`](ReloadDiff.md)

Defined in: [ui/src/api-shared/types/gantt/reload.ts:94](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/reload.ts#L94)

***

### hiveSubjectsUnavailable

> **hiveSubjectsUnavailable**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:108](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/reload.ts#L108)

True when Hive could not supply the module → subject map for this run and
events were left without their subject (and colour) as a result (#662).
A later reload, once Hive is reachable, repairs them.

***

### removedEvents

> **removedEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:98](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/reload.ts#L98)

***

### skippedConflicts

> **skippedConflicts**: `number`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:100](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/reload.ts#L100)

Conflicts left untouched because the user did not override them.

***

### updatedEvents

> **updatedEvents**: `number`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:97](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/reload.ts#L97)
