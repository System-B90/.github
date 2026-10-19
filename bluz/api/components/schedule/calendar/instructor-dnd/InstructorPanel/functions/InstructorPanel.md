[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/InstructorPanel](../index.md) / InstructorPanel

# Function: InstructorPanel()

> **InstructorPanel**(`__namedParameters`): `Element`

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/InstructorPanel.tsx:146](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/instructor-dnd/InstructorPanel.tsx#L146)

Every instructor as a drag source for the schedule calendar, plus the drop
zone that unassigns a dragged person chip. Lives in the schedule side dock,
which keeps it mounted while shut so the search text and scroll position
survive; `open` only gates pointer and a11y access.

## Parameters

### \_\_namedParameters

#### open

`boolean`

## Returns

`Element`

The rendered panel element.
