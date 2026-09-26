[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCurriculumCutStatus

# Type Alias: ApiCurriculumCutStatus

> **ApiCurriculumCutStatus** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:150](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L150)

Cut status for a curriculum, driving the UI toggle between the "cut" and
"pull back" actions. `cut` is true when the linked iteration holds any live
(non-archived) cut event.

## Properties

### count

> **count**: `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:153](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L153)

Number of live cut events in the linked iteration.

***

### cut

> **cut**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:151](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L151)
