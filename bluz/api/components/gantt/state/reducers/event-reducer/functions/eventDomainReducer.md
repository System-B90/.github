[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/reducers/event-reducer](../index.md) / eventDomainReducer

# Function: eventDomainReducer()

> **eventDomainReducer**(`state`, `action`): [`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

Defined in: [ui/src/components/gantt/state/reducers/event-reducer.ts:5](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/components/gantt/state/reducers/event-reducer.ts#L5)

## Parameters

### state

[`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

### action

\{ `payload`: \{ `event`: [`GanttEvent`](../../../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md); `moduleId`: `string`; \}; `type`: `"ADD_EVENT"`; \} \| \{ `payload`: \{ `curriculumId`: `string`; `duration`: `number`; `eventId`: `string`; \}; `type`: `"ALLOCATE_TIME"`; \} \| \{ `payload`: \{ `eventId`: `string`; `moduleId`: `string`; \}; `type`: `"REMOVE_EVENT"`; \} \| \{ `payload`: \{ `id`: `string`; `updates`: `Partial`\<[`GanttEvent`](../../../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)\>; \}; `type`: `"UPDATE_EVENT"`; \}

## Returns

[`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)
