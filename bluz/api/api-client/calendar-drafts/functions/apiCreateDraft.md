[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar-drafts](../index.md) / apiCreateDraft

# Function: apiCreateDraft()

> **apiCreateDraft**(`label`, `events`, `iterationId?`): `Promise`\<[`CalendarDraftSummary`](../../../api-shared/types/type-aliases/CalendarDraftSummary.md)\>

Defined in: [ui/src/api-client/calendar-drafts.ts:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/calendar-drafts.ts#L25)

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
