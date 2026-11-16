[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-dialog/EventTypeField](../index.md) / EventTypeFieldProps

# Type Alias: EventTypeFieldProps

> **EventTypeFieldProps** = `object` & [`EventFieldProps`](../../utils/type-aliases/EventFieldProps.md)

Defined in: [ui/src/components/schedule/event-dialog/EventTypeField.tsx:91](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/schedule/event-dialog/EventTypeField.tsx#L91)

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
