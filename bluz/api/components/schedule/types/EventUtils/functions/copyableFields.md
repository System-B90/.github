[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/types/EventUtils](../index.md) / copyableFields

# Function: copyableFields()

> **copyableFields**(`event`): `Omit`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md), `"ganttCurriculumId"` \| `"ganttEventId"` \| `"ganttOccurrenceDate"` \| `"hiveLesson"` \| `"id"`\>

Defined in: [ui/src/components/schedule/types/EventUtils.ts:156](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/schedule/types/EventUtils.ts#L156)

Everything of an event that a *copy* of it may carry. Strips the id, the
gantt-cut provenance (ganttEventId/ganttOccurrenceDate/ganttCurriculumId,
see EventFactory.ts's invariant) — carrying those over would make the copy
masquerade as the original event — and the Hive lesson, so a copy is
flagged for a lesson of its own instead of silently sharing one (#653). Everything else, including locked/hidden/fake, is copied as-is.

## Parameters

### event

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

The event being copied.

## Returns

`Omit`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md), `"ganttCurriculumId"` \| `"ganttEventId"` \| `"ganttOccurrenceDate"` \| `"hiveLesson"` \| `"id"`\>

The fields a new event may be seeded from.
