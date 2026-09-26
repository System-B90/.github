[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-draft](../../../index.md) / [DbCalendarDraft](../index.md) / update

# Variable: update

> `const` **update**: (`draftId`, `events`, `author`, `controller`, `label?`) => `Promise`\<[`CalendarDraftSummary`](../../../../../api-shared/types/type-aliases/CalendarDraftSummary.md)\> = `updateDraft`

Defined in: [ui/src/api-server/db-calendar-draft.ts:197](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/db-calendar-draft.ts#L197)

Updates an existing shared draft's events (and optionally its label),
re-stamping the last editor. Returns the updated summary.

PATCH semantics: `events === undefined` keeps the stored events untouched.
Replacing them unconditionally meant a label-only update wiped the whole
draft and still reported success (#512).

## Parameters

### draftId

`string`

### events

[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[] \| `undefined`

### author

[`DraftAuthor`](../../../type-aliases/DraftAuthor.md)

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

### label?

`string`

## Returns

`Promise`\<[`CalendarDraftSummary`](../../../../../api-shared/types/type-aliases/CalendarDraftSummary.md)\>
