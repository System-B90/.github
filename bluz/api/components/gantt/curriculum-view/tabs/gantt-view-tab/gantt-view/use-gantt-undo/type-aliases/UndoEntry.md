[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo](../index.md) / UndoEntry

# Type Alias: UndoEntry

> **UndoEntry** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx:19](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx#L19)

A committed action. A step resolving `false` failed (and reported why).

## Properties

### label

> **label**: `string`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx:21](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx#L21)

What happened, in the user's words: "<name> הועבר ליום שני 3.8".

***

### redo

> **redo**: () => `Promise`\<`boolean` \| `void`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx:23](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx#L23)

#### Returns

`Promise`\<`boolean` \| `void`\>

***

### undo

> **undo**: () => `Promise`\<`boolean` \| `void`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx:22](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx#L22)

#### Returns

`Promise`\<`boolean` \| `void`\>
