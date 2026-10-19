[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo](../index.md) / useGanttUndo

# Function: useGanttUndo()

> **useGanttUndo**(): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx:72](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx#L72)

## Returns

### commit

> **commit**: (`entry`) => `void`

Records a just-committed action and confirms it with a snackbar whose
"בטל" button undoes it — the visible counterpart of Ctrl+Z (#809, #810).

#### Parameters

##### entry

[`UndoEntry`](../type-aliases/UndoEntry.md)

#### Returns

`void`

### handleRedo

> **handleRedo**: () => `Promise`\<`void`\>

#### Returns

`Promise`\<`void`\>

### handleUndo

> **handleUndo**: () => `Promise`\<`void`\>

#### Returns

`Promise`\<`void`\>

### pushUndo

> **pushUndo**: (`entry`) => `void`

#### Parameters

##### entry

[`UndoEntry`](../type-aliases/UndoEntry.md)

#### Returns

`void`
