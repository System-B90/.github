[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCurriculumCutStatus

# Type Alias: ApiCurriculumCutStatus

> **ApiCurriculumCutStatus** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:204](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L204)

Cut status for a curriculum, driving the UI toggle between the "cut" and
"pull back" actions. `cut` is true when the linked iteration holds any live
(non-archived) cut event.

## Properties

### count

> **count**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:207](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L207)

Number of live cut events in the linked iteration.

***

### cut

> **cut**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:205](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L205)
