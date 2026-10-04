[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-draft](../../../index.md) / [DbCalendarDraft](../index.md) / get

# Variable: get

> `const` **get**: (`draftId`, `controller`) => `Promise`\<[`CalendarDraft`](../../../../../api-shared/types/type-aliases/CalendarDraft.md)\> = `getDraft`

Defined in: [ui/src/api-server/db-calendar-draft.ts:199](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/db-calendar-draft.ts#L199)

Fetches a single draft including its full events, ready to load.

## Parameters

### draftId

`string`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`CalendarDraft`](../../../../../api-shared/types/type-aliases/CalendarDraft.md)\>
