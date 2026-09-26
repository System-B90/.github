[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/reducers/module-reducer](../index.md) / moduleDomainReducer

# Function: moduleDomainReducer()

> **moduleDomainReducer**(`state`, `action`): [`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

Defined in: [ui/src/components/gantt/state/reducers/module-reducer.ts:6](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/reducers/module-reducer.ts#L6)

## Parameters

### state

[`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

### action

\{ `payload`: \{ `module`: [`GanttModule`](../../../../../../api-shared/types/gantt/models/module/type-aliases/GanttModule.md); `syllabusId`: `string`; \}; `type`: `"ADD_MODULE"`; \} \| \{ `payload`: \{ `curriculumId`: `string`; `duration`: `number`; `moduleId`: `string`; \}; `type`: `"ALLOCATE_TIME_TO_MODULE"`; \} \| \{ `payload`: \{ `eventId`: `string`; `fromModuleId`: `string`; `toModuleId`: `string`; \}; `type`: `"MOVE_EVENT"`; \} \| \{ `payload`: \{ `moduleId`: `string`; `syllabusId`: `string`; \}; `type`: `"REMOVE_MODULE"`; \} \| \{ `payload`: \{ `eventIds`: `string`[]; `moduleId`: `string`; \}; `type`: `"REORDER_EVENTS"`; \} \| \{ `payload`: \{ `id`: `string`; `updates`: `Partial`\<[`GanttModule`](../../../../../../api-shared/types/gantt/models/module/type-aliases/GanttModule.md)\>; \}; `type`: `"UPDATE_MODULE"`; \}

## Returns

[`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)
