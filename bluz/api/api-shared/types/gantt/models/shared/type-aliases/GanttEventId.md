[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/shared](../index.md) / GanttEventId

# Type Alias: GanttEventId

> **GanttEventId** = [`BaseGantItem`](BaseGantItem.md)\[`"id"`\]

Defined in: [ui/src/api-shared/types/gantt/models/shared.ts:11](https://github.com/System-B90/Bluz/blob/ef5f1592ad9f013b150ea581b494f4fff71a8490/ui/src/api-shared/types/gantt/models/shared.ts#L11)

Split out of `event.ts` so `constraint.ts` (which an event's own
`constraints` field references) can depend on the id type without the two
files importing each other.
