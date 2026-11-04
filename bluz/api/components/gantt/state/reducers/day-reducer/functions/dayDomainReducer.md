[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/reducers/day-reducer](../index.md) / dayDomainReducer

# Function: dayDomainReducer()

> **dayDomainReducer**(`state`, `action`): [`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

Defined in: [ui/src/components/gantt/state/reducers/day-reducer.ts:5](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/gantt/state/reducers/day-reducer.ts#L5)

## Parameters

### state

[`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

### action

\{ `payload`: \{ `day`: `object` & [`BaseGantItem`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & `object`; \}; `type`: `"ADD_DAY"`; \} \| \{ `payload`: \{ `dayId`: `string`; \}; `type`: `"REMOVE_DAY"`; \} \| \{ `payload`: \{ `id`: `string`; `updates`: `Partial`\<[`GanttDay`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md)\>; \}; `type`: `"UPDATE_DAY"`; \}

## Returns

[`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)
