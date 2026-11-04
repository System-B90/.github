[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/SliceDialog](../index.md) / SliceDialogProps

# Type Alias: SliceDialogProps

> **SliceDialogProps** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/SliceDialog.tsx:26](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/schedule/event-context-menu/SliceDialog.tsx#L26)

## Properties

### event

> **event**: [`Event`](../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

Defined in: [ui/src/components/schedule/event-context-menu/SliceDialog.tsx:28](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/schedule/event-context-menu/SliceDialog.tsx#L28)

The event being sliced; null while closed.

***

### onClose

> **onClose**: () => `void`

Defined in: [ui/src/components/schedule/event-context-menu/SliceDialog.tsx:29](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/schedule/event-context-menu/SliceDialog.tsx#L29)

#### Returns

`void`

***

### onSliceAfter

> **onSliceAfter**: (`event`, `headWorkingMs`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/SliceDialog.tsx:31](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/schedule/event-context-menu/SliceDialog.tsx#L31)

Cut after this much working time.

#### Parameters

##### event

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

##### headWorkingMs

`number`

#### Returns

`void`
