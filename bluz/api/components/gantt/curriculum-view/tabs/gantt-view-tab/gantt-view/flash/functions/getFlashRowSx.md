[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/flash](../index.md) / getFlashRowSx

# Function: getFlashRowSx()

> **getFlashRowSx**(`theme`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/flash.ts:8](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/flash.ts#L8)

`sx` that briefly flashes a row's sticky label cell when its `data-gantt-flash`
attribute is present. Used to draw the eye after scrolling to an item (from the
unallocated panel). Toggle the attribute imperatively to (re)trigger it.

## Parameters

### theme

`Theme`

## Returns

`object`

### @keyframes ganttFlash

> **@keyframes ganttFlash**: `object`

#### @keyframes ganttFlash.0%

> **0%**: `object`

#### @keyframes ganttFlash.0%.backgroundColor

> **backgroundColor**: `string`

#### @keyframes ganttFlash.100%

> **100%**: `object`

#### @keyframes ganttFlash.100%.backgroundColor

> **backgroundColor**: `string` = `"transparent"`

### &\[data-gantt-flash\] \> td:first-of-type

> **&\[data-gantt-flash\] \> td:first-of-type**: `object`

#### &\[data-gantt-flash\] \> td:first-of-type.animation

> **animation**: `string` = `"ganttFlash 1.5s ease-out"`
