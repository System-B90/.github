[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-scope](../index.md) / calendarWantsEvent

# Function: calendarWantsEvent()

> **calendarWantsEvent**(`event`, `subscribers`): `boolean`

Defined in: [ui/src/api-server/google/google-calendar-scope.ts:31](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/google/google-calendar-scope.ts#L31)

A calendar holds an event when at least one of the users mirroring into it
either syncs everything or is assigned to the event.

## Parameters

### event

`Pick`\<[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md), `"instructors"` \| `"lecturers"`\>

### subscribers

[`GoogleSyncSubscriber`](../type-aliases/GoogleSyncSubscriber.md)[]

## Returns

`boolean`
