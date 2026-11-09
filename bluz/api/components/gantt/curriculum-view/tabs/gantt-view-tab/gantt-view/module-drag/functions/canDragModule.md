[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag](../index.md) / canDragModule

# Function: canDragModule()

> **canDragModule**(`__namedParameters`, `linearDays`): `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag.ts:17](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag.ts#L17)

A רצף זמן module block is draggable only while every event is either
unallocated or mapped inside the timeline. One event outside it would be
left behind (or torn off) by a relative move.

## Parameters

### \_\_namedParameters

`EventPlacement`

### linearDays

`string`[]

## Returns

`boolean`
