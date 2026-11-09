[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-context-menu](../index.md) / ContextMenuSlice

# Type Alias: ContextMenuSlice

> **ContextMenuSlice** = (`event`, `headWorkingMs`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:80](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/event-context-menu/index.tsx#L80)

Cuts one event in two after this much working time — breaks it steps over
don't count. Both pieces keep its fields (#657).

## Parameters

### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

### headWorkingMs

`number`

## Returns

`void`
