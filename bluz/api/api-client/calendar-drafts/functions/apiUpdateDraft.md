[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar-drafts](../index.md) / apiUpdateDraft

# Function: apiUpdateDraft()

> **apiUpdateDraft**(`id`, `events`, `iterationId?`, `label?`, `range?`): `Promise`\<[`CalendarDraftSummary`](../../../api-shared/types/type-aliases/CalendarDraftSummary.md)\>

Defined in: [ui/src/api-client/calendar-drafts.ts:46](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-client/calendar-drafts.ts#L46)

Updates an existing shared draft's events (and optionally its label).

## Parameters

### id

`string`

### events

[`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]

### iterationId?

`string`

### label?

`string`

### range?

[`CalendarDraftRange`](../../../api-shared/types/type-aliases/CalendarDraftRange.md)

## Returns

`Promise`\<[`CalendarDraftSummary`](../../../api-shared/types/type-aliases/CalendarDraftSummary.md)\>
