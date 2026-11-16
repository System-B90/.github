[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/shared](../index.md) / GanttEventId

# Type Alias: GanttEventId

> **GanttEventId** = [`BaseGantItem`](BaseGantItem.md)\[`"id"`\]

Defined in: [ui/src/api-shared/types/gantt/models/shared.ts:11](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-shared/types/gantt/models/shared.ts#L11)

Split out of `event.ts` so `constraint.ts` (which an event's own
`constraints` field references) can depend on the id type without the two
files importing each other.
