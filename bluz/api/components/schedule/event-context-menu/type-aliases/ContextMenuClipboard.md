[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-context-menu](../index.md) / ContextMenuClipboard

# Type Alias: ContextMenuClipboard

> **ContextMenuClipboard** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:74](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/schedule/event-context-menu/index.tsx#L74)

Clipboard (#859): the same actions as Ctrl+C / Ctrl+X / Ctrl+V.

## Properties

### canPaste

> **canPaste**: `boolean`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:79](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/schedule/event-context-menu/index.tsx#L79)

***

### copy

> **copy**: (`event`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:75](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/schedule/event-context-menu/index.tsx#L75)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`void`

***

### cut

> **cut**: (`event`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:76](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/schedule/event-context-menu/index.tsx#L76)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`void`

***

### paste

> **paste**: (`slot`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:78](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/schedule/event-context-menu/index.tsx#L78)

Pastes at the clicked event's start time.

#### Parameters

##### slot

[`PasteSlot`](../../calendar/calendar/paste/type-aliases/PasteSlot.md)

#### Returns

`void`
