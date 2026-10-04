[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-context-menu](../index.md) / EventContextMenuProps

# Type Alias: EventContextMenuProps

> **EventContextMenuProps** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:81](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/schedule/event-context-menu/index.tsx#L81)

## Properties

### clipboard

> **clipboard**: [`ContextMenuClipboard`](ContextMenuClipboard.md)

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:95](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/schedule/event-context-menu/index.tsx#L95)

***

### events

> **events**: [`Event`](../../../../api-shared/types/event/type-aliases/Event.md)[]

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:85](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/schedule/event-context-menu/index.tsx#L85)

The live event list — the target ids are resolved against it.

***

### guards

> **guards**: [`ContextMenuGuards`](ContextMenuGuards.md)

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:96](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/schedule/event-context-menu/index.tsx#L96)

***

### onClose

> **onClose**: () => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:83](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/schedule/event-context-menu/index.tsx#L83)

#### Returns

`void`

***

### onDeleteEvent

> **onDeleteEvent**: (`eventId`, `initiator?`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:91](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/schedule/event-context-menu/index.tsx#L91)

#### Parameters

##### eventId

[`EventId`](../../../../api-shared/types/event/type-aliases/EventId.md)

##### initiator?

[`EventChangeInitiator`](../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md)

#### Returns

`void`

***

### onSaveEvent

> **onSaveEvent**: (`event`, `initiator?`) => [`Event`](../../../../api-shared/types/event/type-aliases/Event.md) \| `undefined` \| `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:87](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/schedule/event-context-menu/index.tsx#L87)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

##### initiator?

[`EventChangeInitiator`](../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md)

#### Returns

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md) \| `undefined` \| `void`

***

### rooms

> **rooms**: [`Room`](../../../../api-shared/types/room/type-aliases/Room.md)[]

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:86](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/schedule/event-context-menu/index.tsx#L86)

***

### target

> **target**: [`ContextMenuTarget`](../use-event-context-menu/type-aliases/ContextMenuTarget.md) \| `null`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:82](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/schedule/event-context-menu/index.tsx#L82)
