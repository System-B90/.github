[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-context-menu](../index.md) / ContextMenuClipboard

# Type Alias: ContextMenuClipboard

> **ContextMenuClipboard** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:57](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/schedule/event-context-menu/index.tsx#L57)

Clipboard (#859): the same actions as Ctrl+C / Ctrl+X / Ctrl+V.

## Properties

### canPaste

> **canPaste**: `boolean`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:62](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/schedule/event-context-menu/index.tsx#L62)

***

### copy

> **copy**: (`event`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:58](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/schedule/event-context-menu/index.tsx#L58)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`void`

***

### cut

> **cut**: (`event`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:59](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/schedule/event-context-menu/index.tsx#L59)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`void`

***

### paste

> **paste**: (`slot`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:61](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/schedule/event-context-menu/index.tsx#L61)

Pastes at the clicked event's start time.

#### Parameters

##### slot

[`PasteSlot`](../../calendar/calendar/paste/type-aliases/PasteSlot.md)

#### Returns

`void`
