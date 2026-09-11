[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/reducers/syllabus-reducer](../index.md) / syllabusDomainReducer

# Function: syllabusDomainReducer()

> **syllabusDomainReducer**(`state`, `action`): [`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

Defined in: [ui/src/components/gantt/state/reducers/syllabus-reducer.ts:5](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/reducers/syllabus-reducer.ts#L5)

## Parameters

### state

[`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

### action

\{ `payload`: \{ `curriculumId`: `string`; `syllabus`: [`GanttSyllabus`](../../../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md); \}; `type`: `"ADD_SYLLABUS"`; \} \| \{ `payload`: `object` & [`NormalizedSyllabusSubtree`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedSyllabusSubtree.md); `type`: `"MERGE_SYLLABUS"`; \} \| \{ `payload`: \{ `curriculumId`: `string`; `syllabusId`: `string`; \}; `type`: `"REMOVE_SYLLABUS"`; \} \| \{ `payload`: \{ `moduleIds`: `string`[]; `syllabusId`: `string`; \}; `type`: `"REORDER_MODULES"`; \} \| \{ `payload`: \{ `id`: `string`; `updates`: `Partial`\<[`GanttSyllabus`](../../../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)\>; \}; `type`: `"UPDATE_SYLLABUS"`; \}

## Returns

[`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)
