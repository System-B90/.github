[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/event-dialog/EventAudienceField](../index.md) / EventAudienceField

# Function: EventAudienceField()

> **EventAudienceField**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/event-dialog/EventAudienceField.tsx:310](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/gantt/event-dialog/EventAudienceField.tsx#L310)

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
