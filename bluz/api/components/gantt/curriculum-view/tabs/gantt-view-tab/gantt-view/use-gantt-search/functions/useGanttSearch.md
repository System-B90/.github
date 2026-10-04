[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-search](../index.md) / useGanttSearch

# Function: useGanttSearch()

> **useGanttSearch**(`__namedParameters`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-search.ts:9](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-search.ts#L9)

## Parameters

### \_\_namedParameters

#### curriculum

[`GanttCurriculum`](../../../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md) \| `undefined`

#### events

`Record`\<`string`, [`GanttEvent`](../../../../../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)\>

#### modules

`Record`\<`string`, [`GanttModule`](../../../../../../../../api-shared/types/gantt/models/module/type-aliases/GanttModule.md)\>

#### syllabuses

`Record`\<`string`, [`GanttSyllabus`](../../../../../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)\>

## Returns

`object`

### isEventVisible

> **isEventVisible**: (`eventId`) => `boolean`

#### Parameters

##### eventId

`string`

#### Returns

`boolean`

### isModuleVisible

> **isModuleVisible**: (`moduleId`) => `boolean`

#### Parameters

##### moduleId

`string`

#### Returns

`boolean`

### isSyllabusVisible

> **isSyllabusVisible**: (`syllabusId`) => `boolean`

#### Parameters

##### syllabusId

`string`

#### Returns

`boolean`

### searchActive

> **searchActive**: `boolean`

### searchQuery

> **searchQuery**: `string`

### setSearchQuery

> **setSearchQuery**: `Dispatch`\<`SetStateAction`\<`string`\>\>
