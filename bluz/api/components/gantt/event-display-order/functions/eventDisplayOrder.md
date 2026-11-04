[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/event-display-order](../index.md) / eventDisplayOrder

# Function: eventDisplayOrder()

> **eventDisplayOrder**(`eventIds`, `events`): `string`[]

Defined in: [ui/src/components/gantt/event-display-order.ts:47](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/gantt/event-display-order.ts#L47)

The module's events, flattened in the order the dialog lists them.

## Parameters

### eventIds

readonly `string`[]

### events

`Readonly`\<`Record`\<`string`, `Pick`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md), `"groupId"`\> \| `undefined`\>\>

## Returns

`string`[]
