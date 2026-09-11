[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/use-event-drop-target](../index.md) / useEventDropTarget

# Function: useEventDropTarget()

> **useEventDropTarget**(`event`, `enabled`, `dropKey?`): `object`

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/use-event-drop-target.ts:21](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/instructor-dnd/use-event-drop-target.ts#L21)

Registers a calendar event as a drop target for instructor drags.
Registration is skipped for locked events, which cannot take assignments
anyway.

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

The droppable ref plus whether a drop here is currently armed.

### isDropTarget

> **isDropTarget**: `boolean`

### isOver

> **isOver**: `boolean`

### setDropRef

> **setDropRef**: (`element`) => `void` = `setNodeRef`

#### Parameters

##### element

`HTMLElement` \| `null`

#### Returns

`void`
