[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar-drafts](../index.md) / apiUpdateDraft

# Function: apiUpdateDraft()

> **apiUpdateDraft**(`id`, `events`, `iterationId?`, `label?`): `Promise`\<[`CalendarDraftSummary`](../../../api-shared/types/type-aliases/CalendarDraftSummary.md)\>

Defined in: [ui/src/api-client/calendar-drafts.ts:41](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-client/calendar-drafts.ts#L41)

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

## Returns

`Promise`\<[`CalendarDraftSummary`](../../../api-shared/types/type-aliases/CalendarDraftSummary.md)\>
