[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/event-dialog/EventMappingField](../index.md) / EventMappingField

# Function: EventMappingField()

> **EventMappingField**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/event-dialog/EventMappingField.tsx:30](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/gantt/event-dialog/EventMappingField.tsx#L30)

Lets the user allocate this event to a week/day directly from the event
dialog, instead of exiting to the רצף זמן tab and dragging it there (#447).
Talks to the mapping API directly rather than through GanttMappingProvider,
since that provider is only mounted inside the gantt-view tab and the event
dialog can be open independently of it.

## Parameters

### \_\_namedParameters

#### curriculumId

`string`

#### eventId

`string`

#### moduleId

`string`

## Returns

`Element`
