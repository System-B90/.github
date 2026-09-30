[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar-drafts](../index.md) / apiGetDraft

# Function: apiGetDraft()

> **apiGetDraft**(`draftId`, `iterationId?`): `Promise`\<\{ `draft`: [`CalendarDraft`](../../../api-shared/types/type-aliases/CalendarDraft.md); `events`: [`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]; \}\>

Defined in: [ui/src/api-client/calendar-drafts.ts:58](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-client/calendar-drafts.ts#L58)

Fetches one draft including its events, mapped into the client Event shape.

## Parameters

### draftId

`string`

### iterationId?

`string`

## Returns

`Promise`\<\{ `draft`: [`CalendarDraft`](../../../api-shared/types/type-aliases/CalendarDraft.md); `events`: [`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]; \}\>
