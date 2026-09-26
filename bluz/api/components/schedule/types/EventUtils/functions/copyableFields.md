[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/types/EventUtils](../index.md) / copyableFields

# Function: copyableFields()

> **copyableFields**(`event`): `Omit`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md), `"ganttCurriculumId"` \| `"ganttEventId"` \| `"ganttOccurrenceDate"` \| `"hiveLesson"` \| `"hiveQueues"` \| `"id"`\>

Defined in: [ui/src/components/schedule/types/EventUtils.ts:118](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/types/EventUtils.ts#L118)

Everything of an event that a *copy* of it may carry. Strips the id, the
gantt-cut provenance (ganttEventId/ganttOccurrenceDate/ganttCurriculumId,
see EventFactory.ts's invariant) — carrying those over would make the copy
masquerade as the original event — and the Hive linkage (hiveLesson/
hiveQueues), which lesson-sync reconciled for the original event only
(#653). Everything else, including locked/hidden/fake, is copied as-is.

## Parameters

### event

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

The event being copied.

## Returns

`Omit`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md), `"ganttCurriculumId"` \| `"ganttEventId"` \| `"ganttOccurrenceDate"` \| `"hiveLesson"` \| `"hiveQueues"` \| `"id"`\>

The fields a new event may be seeded from.
