[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-context-menu](../index.md) / EventContextMenuProps

# Type Alias: EventContextMenuProps

> **EventContextMenuProps** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:53](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/index.tsx#L53)

## Properties

### events

> **events**: [`Event`](../../../../api-shared/types/event/type-aliases/Event.md)[]

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:57](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/index.tsx#L57)

The live event list — the target ids are resolved against it.

***

### onClose

> **onClose**: () => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:55](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/index.tsx#L55)

#### Returns

`void`

***

### onConfirm

> **onConfirm**: (`message`, `options?`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:68](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/index.tsx#L68)

Guards the bulk deletes; resolves false when the user backs out.

#### Parameters

##### message

`string`

##### options?

###### title?

`string`

#### Returns

`Promise`\<`boolean`\>

***

### onDeleteEvent

> **onDeleteEvent**: (`eventId`, `initiator?`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:63](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/index.tsx#L63)

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

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:59](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/index.tsx#L59)

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

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:58](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/index.tsx#L58)

***

### target

> **target**: [`ContextMenuTarget`](../use-event-context-menu/type-aliases/ContextMenuTarget.md) \| `null`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:54](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/index.tsx#L54)
