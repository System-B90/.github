[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/event-dialog/EventAudienceField](../index.md) / EventAudienceField

# Function: EventAudienceField()

> **EventAudienceField**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/event-dialog/EventAudienceField.tsx:310](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/gantt/event-dialog/EventAudienceField.tsx#L310)

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
