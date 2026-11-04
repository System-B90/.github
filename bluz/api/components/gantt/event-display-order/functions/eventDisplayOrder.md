[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/event-display-order](../index.md) / eventDisplayOrder

# Function: eventDisplayOrder()

> **eventDisplayOrder**(`eventIds`, `events`): `string`[]

Defined in: [ui/src/components/gantt/event-display-order.ts:47](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/gantt/event-display-order.ts#L47)

The module's events, flattened in the order the dialog lists them.

## Parameters

### eventIds

readonly `string`[]

### events

`Readonly`\<`Record`\<`string`, `Pick`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md), `"groupId"`\> \| `undefined`\>\>

## Returns

`string`[]
