[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/use-event-selection](../index.md) / EventSelection

# Type Alias: EventSelection

> **EventSelection** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:6](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L6)

## Properties

### clear

> **clear**: () => `void`

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:16](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L16)

#### Returns

`void`

***

### isSelected

> **isSelected**: (`eventId`) => `boolean`

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:9](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L9)

#### Parameters

##### eventId

[`EventId`](../../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`boolean`

***

### selectedEventIds

> **selectedEventIds**: `ReadonlySet`\<[`EventId`](../../../../../api-shared/types/event/type-aliases/EventId.md)\>

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:8](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L8)

Ids the user has explicitly multi-selected (Ctrl/Cmd+click).

***

### selectedEvents

> **selectedEvents**: [`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)[]

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:22](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L22)

The selected events, in calendar order, resolved against the live event
list. Ids whose event is gone (deleted here or by another user) drop out
rather than being handed to an action that would then fail server-side.

***

### selectMany

> **selectMany**: (`eventIds`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:15](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L15)

Replaces the selection with exactly these events (#1000 click-through).

#### Parameters

##### eventIds

[`EventId`](../../../../../api-shared/types/event/type-aliases/EventId.md)[]

#### Returns

`void`

***

### selectOnly

> **selectOnly**: (`eventId`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:11](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L11)

Collapses the selection down to this one event.

#### Parameters

##### eventId

[`EventId`](../../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`void`

***

### toggle

> **toggle**: (`eventId`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:13](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L13)

Ctrl/Cmd+click: adds or removes one event without disturbing the rest.

#### Parameters

##### eventId

[`EventId`](../../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`void`
