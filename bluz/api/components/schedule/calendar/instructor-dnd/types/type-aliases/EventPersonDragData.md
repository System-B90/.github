[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/types](../index.md) / EventPersonDragData

# Type Alias: EventPersonDragData

> **EventPersonDragData** = `object`

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/types.ts:22](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/instructor-dnd/types.ts#L22)

Payload carried by a drag that started on a person chip rendered inside an
event — dragging it away is the unassign gesture.

## Properties

### eventId

> **eventId**: [`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/types.ts:25](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/instructor-dnd/types.ts#L25)

***

### field

> **field**: [`PersonField`](PersonField.md)

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/types.ts:30](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/instructor-dnd/types.ts#L30)

The field the chip currently sits in. A move onto another event keeps
this role rather than defaulting to `instructors` (#628).

***

### kind

> **kind**: `"event-person"`

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/types.ts:23](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/instructor-dnd/types.ts#L23)

***

### personId

> **personId**: [`PersonId`](../../../../../../api-shared/types/event/type-aliases/PersonId.md)

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/types.ts:24](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/instructor-dnd/types.ts#L24)
