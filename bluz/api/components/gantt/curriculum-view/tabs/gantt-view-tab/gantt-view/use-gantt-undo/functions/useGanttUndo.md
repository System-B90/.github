[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo](../index.md) / useGanttUndo

# Function: useGanttUndo()

> **useGanttUndo**(): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx:75](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-undo.tsx#L75)

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
