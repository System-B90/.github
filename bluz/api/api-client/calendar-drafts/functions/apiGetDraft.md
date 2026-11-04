[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar-drafts](../index.md) / apiGetDraft

# Function: apiGetDraft()

> **apiGetDraft**(`draftId`, `iterationId?`): `Promise`\<\{ `draft`: [`CalendarDraft`](../../../api-shared/types/type-aliases/CalendarDraft.md); `events`: [`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]; \}\>

Defined in: [ui/src/api-client/calendar-drafts.ts:67](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-client/calendar-drafts.ts#L67)

Fetches one draft including its events, mapped into the client Event shape.

## Parameters

### draftId

`string`

### iterationId?

`string`

## Returns

`Promise`\<\{ `draft`: [`CalendarDraft`](../../../api-shared/types/type-aliases/CalendarDraft.md); `events`: [`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]; \}\>
