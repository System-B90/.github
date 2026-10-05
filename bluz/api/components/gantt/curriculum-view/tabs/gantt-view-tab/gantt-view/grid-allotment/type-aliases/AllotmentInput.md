[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment](../index.md) / AllotmentInput

# Type Alias: AllotmentInput

> **AllotmentInput** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts:4](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts#L4)

## Properties

### echoDayId?

> `optional` **echoDayId?**: `string`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts:14](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts#L14)

A recurrence echo of the event inside the edited week, if any.

***

### mappings

> **mappings**: [`AllotmentMapping`](AllotmentMapping.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts:10](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts#L10)

The event's own mappings, in timeline order (earliest first).

***

### minutes

> **minutes**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts:6](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts#L6)

The week's new value, in minutes.

***

### splitAcrossWeeks

> **splitAcrossWeeks**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts:15](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts#L15)

***

### weekDays

> **weekDays**: `string`[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts:8](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts#L8)

Days of the edited week, in order.

***

### weekDaysOf

> **weekDaysOf**: (`dayId`) => `string`[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts:12](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts#L12)

Days of the week holding a day, in order.

#### Parameters

##### dayId

`string`

#### Returns

`string`[]
