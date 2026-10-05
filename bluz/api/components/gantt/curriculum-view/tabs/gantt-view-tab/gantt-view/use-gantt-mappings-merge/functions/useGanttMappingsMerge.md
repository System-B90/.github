[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-mappings-merge](../index.md) / useGanttMappingsMerge

# Function: useGanttMappingsMerge()

> **useGanttMappingsMerge**(`globalMappings`, `curriculumId`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-mappings-merge.ts:7](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-mappings-merge.ts#L7)

## Parameters

### globalMappings

`Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

### curriculumId

`string`

## Returns

`object`

### curriculumMappings

> **curriculumMappings**: `Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

### eventMappings

> **eventMappings**: `Record`\<`string`, `string`\>

### moduleMappings

> **moduleMappings**: `Record`\<`string`, `string`[]\>
