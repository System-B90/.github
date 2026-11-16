[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/event-display-order](../index.md) / eventDisplayOrder

# Function: eventDisplayOrder()

> **eventDisplayOrder**(`eventIds`, `events`): `string`[]

Defined in: [ui/src/components/gantt/event-display-order.ts:47](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/gantt/event-display-order.ts#L47)

The module's events, flattened in the order the dialog lists them.

## Parameters

### eventIds

readonly `string`[]

### events

`Readonly`\<`Record`\<`string`, `Pick`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md), `"groupId"`\> \| `undefined`\>\>

## Returns

`string`[]
