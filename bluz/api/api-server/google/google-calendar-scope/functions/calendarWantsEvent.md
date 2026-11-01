[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-scope](../index.md) / calendarWantsEvent

# Function: calendarWantsEvent()

> **calendarWantsEvent**(`event`, `subscribers`): `boolean`

Defined in: [ui/src/api-server/google/google-calendar-scope.ts:31](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/google/google-calendar-scope.ts#L31)

A calendar holds an event when at least one of the users mirroring into it
either syncs everything or is assigned to the event.

## Parameters

### event

`Pick`\<[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md), `"instructors"` \| `"lecturers"`\>

### subscribers

[`GoogleSyncSubscriber`](../type-aliases/GoogleSyncSubscriber.md)[]

## Returns

`boolean`
