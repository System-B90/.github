[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-dialog/room-reservation](../index.md) / reservationBlockedReason

# Function: reservationBlockedReason()

> **reservationBlockedReason**(`event`, `reserver`): `string`

Defined in: [ui/src/components/schedule/event-dialog/room-reservation.ts:14](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/components/schedule/event-dialog/room-reservation.ts#L14)

Why the reservation can't be saved yet, or "" when it can.

## Parameters

### event

`Partial`\<`Pick`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md), `"endTime"` \| `"rooms"` \| `"startTime"`\>\>

### reserver

[`ReserverDetails`](../../../../settings-dialog/tabs/global/room-settings/reservations/ReserverFields/type-aliases/ReserverDetails.md)

## Returns

`string`
