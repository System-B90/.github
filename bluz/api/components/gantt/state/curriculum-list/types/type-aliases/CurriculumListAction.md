[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/curriculum-list/types](../index.md) / CurriculumListAction

# Type Alias: CurriculumListAction

> **CurriculumListAction** = \{ `payload`: [`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md); `type`: `"ADD_CURRICULUM"`; \} \| \{ `payload`: [`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md); `type`: `"REMOVE_CURRICULUM"`; \} \| \{ `payload`: `Record`\<[`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md), [`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)\>; `type`: `"SET_CURRICULUMS"`; \} \| \{ `payload`: `null` \| `string`; `type`: `"SET_ERROR"`; \} \| \{ `payload`: `boolean`; `type`: `"SET_LOADING"`; \} \| \{ `payload`: \{ `id`: [`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md); `updates`: `Partial`\<[`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)\>; \}; `type`: `"UPDATE_CURRICULUM"`; \}

Defined in: [ui/src/components/gantt/state/curriculum-list/types.ts:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/types.ts#L16)
