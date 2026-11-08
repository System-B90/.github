[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/use-event-drop-target](../index.md) / useEventDropTarget

# Function: useEventDropTarget()

> **useEventDropTarget**(`event`, `enabled`, `dropKey?`): `object`

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/use-event-drop-target.ts:33](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/schedule/calendar/instructor-dnd/use-event-drop-target.ts#L33)

Makes a calendar event a drop target for instructor drags. Locked events
take drops too: the lock pins timing, not people (#1016).

The droppable itself registers through `registration`, rendered as a
[DroppableRegistration](../../../../../base/dnd/drag-over-store/functions/DroppableRegistration.md) leaf: dnd-kit re-renders whoever registers a
droppable on every change to the drag, and the tile must not be that (#955
did the same for grid drags). What the tile draws reads from the drag-over
store, so it re-renders only when a drag starts or ends and when the drag
enters or leaves it.

## Parameters

### event

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

The event being rendered.

### enabled

`boolean`

Whether this render should accept drops.

### dropKey?

`string` = `event.id`

Distinguishes co-existing drop targets for the same event —
               an event split across breaks is drawn as several boxes, and
               each must be droppable in its own right. Defaults to the
               event id.

## Returns

`object`

The element ref, the registration's props, and whether a drop
         here is currently armed / under the pointer.

### isDropTarget

> **isDropTarget**: `boolean`

### isOver

> **isOver**: `boolean`

### registration

> **registration**: `object`

#### registration.data

> **data**: [`EventDropData`](../../types/type-aliases/EventDropData.md)

#### registration.disabled

> **disabled**: `boolean` = `!enabled`

#### registration.id

> **id**: `string`

#### registration.slot

> **slot**: [`NodeSlot`](../../../../../base/dnd/drag-over-store/type-aliases/NodeSlot.md)

### setDropRef

> **setDropRef**: `RefCallback`\<`HTMLElement`\> = `slot.setNode`
