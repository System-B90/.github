[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-dialog/EventTypeField](../index.md) / EventTypeFieldProps

# Type Alias: EventTypeFieldProps

> **EventTypeFieldProps** = `object` & [`EventFieldProps`](../../utils/type-aliases/EventFieldProps.md)

Defined in: [ui/src/components/schedule/event-dialog/EventTypeField.tsx:97](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/schedule/event-dialog/EventTypeField.tsx#L97)

## Type Declaration

### onReservingChange?

> `optional` **onReservingChange?**: (`reserving`) => `void`

Offers the שיריון כיתה pseudo-type, and reports picking it or leaving
it. Omitted (a saved event) → not offered: an event never turns into a
reservation.

#### Parameters

##### reserving

`boolean`

#### Returns

`void`

### reserving?

> `optional` **reserving?**: `boolean`

The dialog is in its שיריון כיתה mode (see `room-reservation.ts`).
