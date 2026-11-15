[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-dialog/room-reservation](../index.md) / reservationBlockedReason

# Function: reservationBlockedReason()

> **reservationBlockedReason**(`event`, `reserver`): `string`

Defined in: [ui/src/components/schedule/event-dialog/room-reservation.ts:14](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/schedule/event-dialog/room-reservation.ts#L14)

Why the reservation can't be saved yet, or "" when it can.

## Parameters

### event

`Partial`\<`Pick`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md), `"endTime"` \| `"rooms"` \| `"startTime"`\>\>

### reserver

[`ReserverDetails`](../../../../settings-dialog/tabs/global/room-settings/reservations/ReserverFields/type-aliases/ReserverDetails.md)

## Returns

`string`
