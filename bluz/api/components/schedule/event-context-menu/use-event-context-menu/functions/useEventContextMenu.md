[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/use-event-context-menu](../index.md) / useEventContextMenu

# Function: useEventContextMenu()

> **useEventContextMenu**(`selection`): `object`

Defined in: [ui/src/components/schedule/event-context-menu/use-event-context-menu.ts:26](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/use-event-context-menu.ts#L26)

Owns the right-click menu's open state and decides what a right-click acts
on (#706): inside an existing multi-selection it adopts the whole selection,
anywhere else it collapses the selection onto the event that was clicked —
the same rule file managers and design tools use.

## Parameters

### selection

[`EventSelection`](../../use-event-selection/type-aliases/EventSelection.md)

The calendar's multi-selection.

## Returns

`object`

The current target, plus open/close operations.

### close

> **close**: () => `void`

#### Returns

`void`

### openAt

> **openAt**: (`event`, `clientX`, `clientY`) => `void`

#### Parameters

##### event

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

##### clientX

`number`

##### clientY

`number`

#### Returns

`void`

### target

> **target**: [`ContextMenuTarget`](../type-aliases/ContextMenuTarget.md) \| `null`
