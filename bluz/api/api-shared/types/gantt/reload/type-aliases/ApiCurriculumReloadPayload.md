[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / ApiCurriculumReloadPayload

# Type Alias: ApiCurriculumReloadPayload

> **ApiCurriculumReloadPayload** = `object`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:79](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/types/gantt/reload.ts#L79)

## Properties

### dryRun?

> `optional` **dryRun?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:81](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/types/gantt/reload.ts#L81)

Compute the diff and write nothing.

***

### force?

> `optional` **force?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:88](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/types/gantt/reload.ts#L88)

Plan around unmapped events / unsatisfied recurrences, as with the cut.

***

### overrideEventIds?

> `optional` **overrideEventIds?**: `string`[]

Defined in: [ui/src/api-shared/types/gantt/reload.ts:86](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/types/gantt/reload.ts#L86)

Manually-edited events the user chose to overwrite anyway. Their
conflicts are applied instead of skipped.
