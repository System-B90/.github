[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/frozen-columns](../index.md) / FrozenColumns

# Type Alias: FrozenColumns

> **FrozenColumns** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/frozen-columns.ts:6](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/frozen-columns.ts#L6)

Frozen leading columns of the gantt table (#913): the course columns, the
title, and the required/allocated hours stay put while the weeks scroll
sideways beneath them, the way the header rows stay put vertically.

## Properties

### offsets

> **offsets**: `number`[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/frozen-columns.ts:8](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/frozen-columns.ts#L8)

Inline-start offset (px) of each frozen column, in column order.

***

### width

> **width**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/frozen-columns.ts:10](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/frozen-columns.ts#L10)

Total width (px) of the frozen block; the weeks scroll under it.
