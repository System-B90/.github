[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-draft](../../../index.md) / [DbCalendarDraft](../index.md) / get

# Variable: get

> `const` **get**: (`draftId`, `controller`) => `Promise`\<[`CalendarDraft`](../../../../../api-shared/types/type-aliases/CalendarDraft.md)\> = `getDraft`

Defined in: [ui/src/api-server/db-calendar-draft.ts:237](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/db-calendar-draft.ts#L237)

Fetches a single draft including its full events, ready to load.

## Parameters

### draftId

`string`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`CalendarDraft`](../../../../../api-shared/types/type-aliases/CalendarDraft.md)\>
