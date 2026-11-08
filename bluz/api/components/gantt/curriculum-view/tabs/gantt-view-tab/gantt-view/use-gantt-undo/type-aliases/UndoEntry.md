[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo](../index.md) / UndoEntry

# Type Alias: UndoEntry

> **UndoEntry** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx:21](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx#L21)

A committed action. A step resolving `false` failed (and reported why).

## Properties

### label

> **label**: `string`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx:23](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx#L23)

What happened, in the user's words: "<name> הועבר ליום שני 3.8".

***

### redo

> **redo**: () => `Promise`\<`boolean` \| `void`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx:25](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx#L25)

#### Returns

`Promise`\<`boolean` \| `void`\>

***

### undo

> **undo**: () => `Promise`\<`boolean` \| `void`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx:24](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx#L24)

#### Returns

`Promise`\<`boolean` \| `void`\>
