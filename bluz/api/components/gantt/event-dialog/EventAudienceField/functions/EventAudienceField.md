[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/event-dialog/EventAudienceField](../index.md) / EventAudienceField

# Function: EventAudienceField()

> **EventAudienceField**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/event-dialog/EventAudienceField.tsx:246](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/event-dialog/EventAudienceField.tsx#L246)

Who an event is for: the whole syllabus, a split into
shuffles (one copy per shuffle, aligned in the same block), or only some of
the syllabus' courses — which need not align with the other courses, and
where shuffles no longer apply.

## Parameters

### \_\_namedParameters

#### event

[`GanttEvent`](../../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)

#### eventId

`string`

#### moduleId

`string`

#### syllabus

[`GanttSyllabus`](../../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md) \| `null` \| `undefined`

## Returns

`Element`
