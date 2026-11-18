[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-draft](../../../index.md) / [DbCalendarDraft](../index.md) / list

# Variable: list

> `const` **list**: (`controller`, `iterationId?`) => `Promise`\<[`CalendarDraftSummary`](../../../../../api-shared/types/type-aliases/CalendarDraftSummary.md)[]\> = `listDrafts`

Defined in: [ui/src/api-server/db-calendar-draft.ts:236](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-server/db-calendar-draft.ts#L236)

Lists shared drafts newest-updated-first, without their events payload.

## Parameters

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

### iterationId?

`string`

## Returns

`Promise`\<[`CalendarDraftSummary`](../../../../../api-shared/types/type-aliases/CalendarDraftSummary.md)[]\>
