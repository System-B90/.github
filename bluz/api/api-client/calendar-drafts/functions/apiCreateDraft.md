[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar-drafts](../index.md) / apiCreateDraft

# Function: apiCreateDraft()

> **apiCreateDraft**(`label`, `events`, `iterationId?`): `Promise`\<[`CalendarDraftSummary`](../../../api-shared/types/type-aliases/CalendarDraftSummary.md)\>

Defined in: [ui/src/api-client/calendar-drafts.ts:25](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-client/calendar-drafts.ts#L25)

Creates a new shared draft capturing the supplied events.

## Parameters

### label

`string`

### events

[`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]

### iterationId?

`string`

## Returns

`Promise`\<[`CalendarDraftSummary`](../../../api-shared/types/type-aliases/CalendarDraftSummary.md)\>
