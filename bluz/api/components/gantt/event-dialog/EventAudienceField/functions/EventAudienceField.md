[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/event-dialog/EventAudienceField](../index.md) / EventAudienceField

# Function: EventAudienceField()

> **EventAudienceField**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/event-dialog/EventAudienceField.tsx:310](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/event-dialog/EventAudienceField.tsx#L310)

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
