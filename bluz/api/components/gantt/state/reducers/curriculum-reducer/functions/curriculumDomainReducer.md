[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/reducers/curriculum-reducer](../index.md) / curriculumDomainReducer

# Function: curriculumDomainReducer()

> **curriculumDomainReducer**(`state`, `action`): [`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

Defined in: [ui/src/components/gantt/state/reducers/curriculum-reducer.ts:4](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/state/reducers/curriculum-reducer.ts#L4)

## Parameters

### state

[`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

### action

\{ `payload`: [`ApiCurriculum`](../../../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md); `type`: `"SET_DATA"`; \} \| \{ `payload`: \{ `id`: `string`; `updates`: `Partial`\<[`GanttCurriculum`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md)\>; \}; `type`: `"UPDATE_CURRICULUM"`; \}

## Returns

[`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)
