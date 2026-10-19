[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / ApiCurriculumReloadPayload

# Type Alias: ApiCurriculumReloadPayload

> **ApiCurriculumReloadPayload** = `object`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:84](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L84)

## Properties

### dryRun?

> `optional` **dryRun?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:86](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L86)

Compute the diff and write nothing.

***

### force?

> `optional` **force?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:93](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L93)

Plan around unmapped events / unsatisfied recurrences, as with the cut.

***

### overrideEventIds?

> `optional` **overrideEventIds?**: `string`[]

Defined in: [ui/src/api-shared/types/gantt/reload.ts:91](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L91)

Manually-edited events the user chose to overwrite anyway. Their
conflicts are applied instead of skipped.

***

### weekId?

> `optional` **weekId?**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:95](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/reload.ts#L95)

Reload only this timeline week; omitted ⇒ the whole curriculum.
