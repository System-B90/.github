[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/event-display-order](../index.md) / eventDisplayOrder

# Function: eventDisplayOrder()

> **eventDisplayOrder**(`eventIds`, `events`): `string`[]

Defined in: [ui/src/components/gantt/event-display-order.ts:47](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/gantt/event-display-order.ts#L47)

The module's events, flattened in the order the dialog lists them.

## Parameters

### eventIds

readonly `string`[]

### events

`Readonly`\<`Record`\<`string`, `Pick`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md), `"groupId"`\> \| `undefined`\>\>

## Returns

`string`[]
