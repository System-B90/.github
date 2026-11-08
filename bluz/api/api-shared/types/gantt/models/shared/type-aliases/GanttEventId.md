[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/shared](../index.md) / GanttEventId

# Type Alias: GanttEventId

> **GanttEventId** = [`BaseGantItem`](BaseGantItem.md)\[`"id"`\]

Defined in: [ui/src/api-shared/types/gantt/models/shared.ts:11](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types/gantt/models/shared.ts#L11)

Split out of `event.ts` so `constraint.ts` (which an event's own
`constraints` field references) can depend on the id type without the two
files importing each other.
