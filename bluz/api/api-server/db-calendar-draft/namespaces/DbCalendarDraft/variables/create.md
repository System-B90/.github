[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-draft](../../../index.md) / [DbCalendarDraft](../index.md) / create

# Variable: create

> `const` **create**: (`label`, `events`, `author`, `controller`, `iterationId?`, `range?`) => `Promise`\<[`CalendarDraftSummary`](../../../../../api-shared/types/type-aliases/CalendarDraftSummary.md)\> = `createDraft`

Defined in: [ui/src/api-server/db-calendar-draft.ts:234](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/db-calendar-draft.ts#L234)

Creates a new shared draft capturing the supplied events. Drafts are shared
across all users of the iteration (multi-user).

## Parameters

### label

`string`

### events

[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

### author

[`DraftAuthor`](../../../type-aliases/DraftAuthor.md)

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

### iterationId?

`string`

### range?

[`CalendarDraftRange`](../../../../../api-shared/types/type-aliases/CalendarDraftRange.md)

## Returns

`Promise`\<[`CalendarDraftSummary`](../../../../../api-shared/types/type-aliases/CalendarDraftSummary.md)\>
