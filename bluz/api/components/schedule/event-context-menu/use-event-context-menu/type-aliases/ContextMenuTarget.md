[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/use-event-context-menu](../index.md) / ContextMenuTarget

# Type Alias: ContextMenuTarget

> **ContextMenuTarget** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/use-event-context-menu.ts:7](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/use-event-context-menu.ts#L7)

## Properties

### eventIds

> **eventIds**: [`EventId`](../../../../../api-shared/types/event/type-aliases/EventId.md)[]

Defined in: [ui/src/components/schedule/event-context-menu/use-event-context-menu.ts:15](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/use-event-context-menu.ts#L15)

Ids only, never the events themselves: the menu re-resolves them against
live state on every render, so toggling a marker with the menu still open
redraws its own checkmark instead of showing a snapshot taken at open.

***

### position

> **position**: `object`

Defined in: [ui/src/components/schedule/event-context-menu/use-event-context-menu.ts:9](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/use-event-context-menu.ts#L9)

Viewport coordinates of the click that opened the menu.

#### left

> **left**: `number`

#### top

> **top**: `number`
