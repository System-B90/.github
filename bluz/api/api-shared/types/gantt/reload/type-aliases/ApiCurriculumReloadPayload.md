[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / ApiCurriculumReloadPayload

# Type Alias: ApiCurriculumReloadPayload

> **ApiCurriculumReloadPayload** = `object`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:84](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/gantt/reload.ts#L84)

## Properties

### dryRun?

> `optional` **dryRun?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:86](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/gantt/reload.ts#L86)

Compute the diff and write nothing.

***

### force?

> `optional` **force?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:93](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/gantt/reload.ts#L93)

Plan around unmapped events / unsatisfied recurrences, as with the cut.

***

### overrideEventIds?

> `optional` **overrideEventIds?**: `string`[]

Defined in: [ui/src/api-shared/types/gantt/reload.ts:91](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/gantt/reload.ts#L91)

Manually-edited events the user chose to overwrite anyway. Their
conflicts are applied instead of skipped.

***

### parkNonTemplate?

> `optional` **parkNonTemplate?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:105](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/gantt/reload.ts#L105)

Place only what the template places and park the rest, or (false)
auto-place it. Omitted ⇒ whether an event is parked is left as is.

***

### templateId?

> `optional` **templateId?**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:100](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/gantt/reload.ts#L100)

Re-plan the reloaded weeks under this week template instead of the one
each was cut with (#997). Omitted ⇒ every week keeps its own template.

***

### weekId?

> `optional` **weekId?**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:95](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/gantt/reload.ts#L95)

Reload only this timeline week; omitted ⇒ the whole curriculum.
