[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag](../index.md) / canDragModule

# Function: canDragModule()

> **canDragModule**(`__namedParameters`, `linearDays`): `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag.ts:17](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-drag.ts#L17)

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
