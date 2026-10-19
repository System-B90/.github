[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/SliceDialog](../index.md) / SliceDialogProps

# Type Alias: SliceDialogProps

> **SliceDialogProps** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/SliceDialog.tsx:23](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/SliceDialog.tsx#L23)

## Properties

### event

> **event**: [`Event`](../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

Defined in: [ui/src/components/schedule/event-context-menu/SliceDialog.tsx:25](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/SliceDialog.tsx#L25)

The event being sliced; null while closed.

***

### onClose

> **onClose**: () => `void`

Defined in: [ui/src/components/schedule/event-context-menu/SliceDialog.tsx:26](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/SliceDialog.tsx#L26)

#### Returns

`void`

***

### onSliceAfter

> **onSliceAfter**: (`event`, `headWorkingMs`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/SliceDialog.tsx:28](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/SliceDialog.tsx#L28)

Cut after this much working time.

#### Parameters

##### event

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

##### headWorkingMs

`number`

#### Returns

`void`
