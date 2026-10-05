[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-draft](../../../index.md) / [DbCalendarDraft](../index.md) / get

# Variable: get

> `const` **get**: (`draftId`, `controller`) => `Promise`\<[`CalendarDraft`](../../../../../api-shared/types/type-aliases/CalendarDraft.md)\> = `getDraft`

Defined in: [ui/src/api-server/db-calendar-draft.ts:199](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/db-calendar-draft.ts#L199)

Fetches a single draft including its full events, ready to load.

## Parameters

### draftId

`string`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`CalendarDraft`](../../../../../api-shared/types/type-aliases/CalendarDraft.md)\>
