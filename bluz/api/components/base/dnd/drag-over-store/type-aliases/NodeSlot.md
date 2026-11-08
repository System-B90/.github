[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/dnd/drag-over-store](../index.md) / NodeSlot

# Type Alias: NodeSlot

> **NodeSlot** = `object`

Defined in: [ui/src/components/base/dnd/drag-over-store.tsx:132](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/dnd/drag-over-store.tsx#L132)

Hands the element a ref lands on to a dnd-kit registration rendered
elsewhere: `setNode` is the ref, and `connect` is how a
[DroppableRegistration](../functions/DroppableRegistration.md) (or a handle-only `DraggableBox`) receives
the element, now and whenever it changes.

## Properties

### connect

> **connect**: (`attach`) => () => `void`

Defined in: [ui/src/components/base/dnd/drag-over-store.tsx:134](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/dnd/drag-over-store.tsx#L134)

#### Parameters

##### attach

(`node`) => `void`

#### Returns

() => `void`

***

### setNode

> **setNode**: `RefCallback`\<`HTMLElement`\>

Defined in: [ui/src/components/base/dnd/drag-over-store.tsx:133](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/dnd/drag-over-store.tsx#L133)
