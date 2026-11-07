[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/event-display-order](../index.md) / groupEventBlocks

# Function: groupEventBlocks()

> **groupEventBlocks**(`eventIds`, `events`): [`EventDisplayBlock`](../type-aliases/EventDisplayBlock.md)[]

Defined in: [ui/src/components/gantt/event-display-order.ts:21](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/gantt/event-display-order.ts#L21)

Splits `eventIds` (the module's saved order) into top-level blocks: a
group sits where its first member is, with every member gathered under it.

## Parameters

### eventIds

readonly `string`[]

### events

`Readonly`\<`Record`\<`string`, `Pick`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md), `"groupId"`\> \| `undefined`\>\>

## Returns

[`EventDisplayBlock`](../type-aliases/EventDisplayBlock.md)[]
