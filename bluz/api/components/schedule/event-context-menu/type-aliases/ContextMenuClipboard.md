[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-context-menu](../index.md) / ContextMenuClipboard

# Type Alias: ContextMenuClipboard

> **ContextMenuClipboard** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:68](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-context-menu/index.tsx#L68)

Clipboard (#859): the same actions as Ctrl+C / Ctrl+X / Ctrl+V.

## Properties

### canPaste

> **canPaste**: `boolean`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:73](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-context-menu/index.tsx#L73)

***

### copy

> **copy**: (`event`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:69](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-context-menu/index.tsx#L69)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`void`

***

### cut

> **cut**: (`event`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:70](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-context-menu/index.tsx#L70)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`void`

***

### paste

> **paste**: (`slot`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:72](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-context-menu/index.tsx#L72)

Pastes at the clicked event's start time.

#### Parameters

##### slot

[`PasteSlot`](../../calendar/calendar/paste/type-aliases/PasteSlot.md)

#### Returns

`void`
