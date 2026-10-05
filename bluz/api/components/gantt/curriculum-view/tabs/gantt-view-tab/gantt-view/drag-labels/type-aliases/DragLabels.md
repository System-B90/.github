[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drag-labels](../index.md) / DragLabels

# Type Alias: DragLabels

> **DragLabels** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drag-labels.ts:14](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drag-labels.ts#L14)

## Properties

### dayLabel

> **dayLabel**: (`dayId`) => `string`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drag-labels.ts:18](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drag-labels.ts#L18)

"יום שני 3.8" (date omitted when the curriculum has no start date).

#### Parameters

##### dayId

`string`

#### Returns

`string`

***

### itemName

> **itemName**: (`item`) => `string`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drag-labels.ts:16](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/drag-labels.ts#L16)

Quoted title of the dragged module or event.

#### Parameters

##### item

\{ `eventId?`: `null` \| `string`; `moduleId?`: `string`; \} \| `undefined`

#### Returns

`string`
