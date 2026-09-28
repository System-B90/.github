[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/reducers/week-reducer](../index.md) / weekDomainReducer

# Function: weekDomainReducer()

> **weekDomainReducer**(`state`, `action`): [`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

Defined in: [ui/src/components/gantt/state/reducers/week-reducer.ts:5](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/components/gantt/state/reducers/week-reducer.ts#L5)

## Parameters

### state

[`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

### action

\{ `payload`: \{ `curriculumId`: `string`; `week`: `object` & [`BaseGantItem`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & `object`; \}; `type`: `"ADD_WEEK"`; \} \| \{ `payload`: \{ `curriculumId`: `string`; `weekId`: `string`; \}; `type`: `"REMOVE_WEEK"`; \} \| \{ `payload`: \{ `id`: `string`; `updates`: `Partial`\<[`GanttWeek`](../../../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeek.md)\>; \}; `type`: `"UPDATE_WEEK"`; \}

## Returns

[`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)
