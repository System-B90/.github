[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/event-dialog/DetailsForm](../index.md) / EventDetailsForm

# Function: EventDetailsForm()

> **EventDetailsForm**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/event-dialog/DetailsForm.tsx:27](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/event-dialog/DetailsForm.tsx#L27)

The always-visible core of the event dialog: identity (name / type /
duration) on the first row, assignment (orchestrator / shuffles / flags)
on the second. Everything optional lives in collapsible sections below.

## Parameters

### \_\_namedParameters

#### commit

(`updates`) => `void`

#### event

[`GanttEvent`](../../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)

#### leadInstructorIds

`number`[]

#### localTitle

`string`

#### setLocalTitle

(`v`) => `void`

## Returns

`Element`
