[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-dialog/room-reservation](../index.md) / reservationPayloadsFor

# Function: reservationPayloadsFor()

> **reservationPayloadsFor**(`event`, `reserver`): [`ApiReservationCreatePayload`](../../../../../api-shared/types/reservation/type-aliases/ApiReservationCreatePayload.md)[]

Defined in: [ui/src/components/schedule/event-dialog/room-reservation.ts:30](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/components/schedule/event-dialog/room-reservation.ts#L30)

The reservations a שיריון כיתה dialog makes: one per picked room, all over
the dialog's times. Call only once `reservationBlockedReason` is "".

## Parameters

### event

`Partial`\<`Pick`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md), `"endTime"` \| `"rooms"` \| `"startTime"`\>\>

### reserver

[`ReserverDetails`](../../../../settings-dialog/tabs/global/room-settings/reservations/ReserverFields/type-aliases/ReserverDetails.md)

## Returns

[`ApiReservationCreatePayload`](../../../../../api-shared/types/reservation/type-aliases/ApiReservationCreatePayload.md)[]
