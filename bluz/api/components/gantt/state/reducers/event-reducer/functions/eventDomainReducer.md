[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/reducers/event-reducer](../index.md) / eventDomainReducer

# Function: eventDomainReducer()

> **eventDomainReducer**(`state`, `action`): [`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

Defined in: [ui/src/components/gantt/state/reducers/event-reducer.ts:5](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/reducers/event-reducer.ts#L5)

## Parameters

### state

[`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

### action

\{ `payload`: \{ `event`: [`GanttEvent`](../../../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md); `moduleId`: `string`; \}; `type`: `"ADD_EVENT"`; \} \| \{ `payload`: \{ `curriculumId`: `string`; `duration`: `number`; `eventId`: `string`; \}; `type`: `"ALLOCATE_TIME"`; \} \| \{ `payload`: \{ `eventId`: `string`; `moduleId`: `string`; \}; `type`: `"REMOVE_EVENT"`; \} \| \{ `payload`: \{ `id`: `string`; `updates`: `Partial`\<[`GanttEvent`](../../../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)\>; \}; `type`: `"UPDATE_EVENT"`; \}

## Returns

[`NormalizedStore`](../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)
