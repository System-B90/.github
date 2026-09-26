[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/use-event-selection](../index.md) / EventSelection

# Type Alias: EventSelection

> **EventSelection** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:6](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L6)

## Properties

### clear

> **clear**: () => `void`

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:14](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L14)

#### Returns

`void`

***

### isSelected

> **isSelected**: (`eventId`) => `boolean`

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:9](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L9)

#### Parameters

##### eventId

[`EventId`](../../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`boolean`

***

### selectedEventIds

> **selectedEventIds**: `ReadonlySet`\<[`EventId`](../../../../../api-shared/types/event/type-aliases/EventId.md)\>

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:8](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L8)

Ids the user has explicitly multi-selected (Ctrl/Cmd+click).

***

### selectedEvents

> **selectedEvents**: [`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)[]

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:20](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L20)

The selected events, in calendar order, resolved against the live event
list. Ids whose event is gone (deleted here or by another user) drop out
rather than being handed to an action that would then fail server-side.

***

### selectOnly

> **selectOnly**: (`eventId`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:11](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L11)

Collapses the selection down to this one event.

#### Parameters

##### eventId

[`EventId`](../../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`void`

***

### toggle

> **toggle**: (`eventId`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:13](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L13)

Ctrl/Cmd+click: adds or removes one event without disturbing the rest.

#### Parameters

##### eventId

[`EventId`](../../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`void`
