[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/dnd/DraggableBox](../index.md) / DraggableBoxProps

# Type Alias: DraggableBoxProps

> **DraggableBoxProps** = `Omit`\<`BoxProps`, `"onKeyDown"` \| `"onPointerDown"` \| `"ref"`\> & `object`

Defined in: [ui/src/components/base/dnd/DraggableBox.tsx:21](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/base/dnd/DraggableBox.tsx#L21)

## Type Declaration

### bareWhenDisabled?

> `optional` **bareWhenDisabled?**: `boolean`

Drop dnd-kit's listeners *and* its button attributes while disabled.

### drag

> **drag**: `UseDraggableArguments`

What `useDraggable` registers.

### draggingSx?

> `optional` **draggingSx?**: `SxProps`\<`Theme`\>

Merged over `sx` while this is the item being dragged.

### nodeSlot?

> `optional` **nodeSlot?**: [`NodeSlot`](../../drag-over-store/type-aliases/NodeSlot.md)

Make this box only the drag *handle*: the element behind `nodeSlot`
is what dnd-kit measures and moves, read `useIsDragging` there.

### onKeyDown?

> `optional` **onKeyDown?**: (`event`, `state`) => `void`

Runs before dnd-kit's; `preventDefault()` keeps the key from it. Any
other handler for an event dnd-kit also listens to runs first the same
way; these two are told whether this item is being dragged.

#### Parameters

##### event

`ReactKeyboardEvent`\<`HTMLElement`\>

##### state

[`DraggableState`](DraggableState.md)

#### Returns

`void`

### onPointerDown?

> `optional` **onPointerDown?**: (`event`, `state`) => `void`

Runs before dnd-kit's; `preventDefault()` keeps the press from it.

#### Parameters

##### event

`ReactPointerEvent`\<`HTMLElement`\>

##### state

[`DraggableState`](DraggableState.md)

#### Returns

`void`

### ref?

> `optional` **ref?**: `Ref`\<`HTMLElement`\>

For a wrapping `Tooltip`, which anchors to the element.

### transformStyle?

> `optional` **transformStyle?**: (`transform`, `isDragging`) => `CSSProperties`

Inline style for dnd-kit's live offset, for an item that moves with the
pointer itself rather than through a `DragOverlay`. Inline, never `sx`:
a new offset in `sx` is a new emotion class on every pointer move.

#### Parameters

##### transform

`Transform`

##### isDragging

`boolean`

#### Returns

`CSSProperties`
