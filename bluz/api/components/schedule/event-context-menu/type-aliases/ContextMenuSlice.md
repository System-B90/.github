[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-context-menu](../index.md) / ContextMenuSlice

# Type Alias: ContextMenuSlice

> **ContextMenuSlice** = (`event`, `headWorkingMs`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:80](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-context-menu/index.tsx#L80)

Cuts one event in two after this much working time — breaks it steps over
don't count. Both pieces keep its fields (#657).

## Parameters

### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

### headWorkingMs

`number`

## Returns

`void`
