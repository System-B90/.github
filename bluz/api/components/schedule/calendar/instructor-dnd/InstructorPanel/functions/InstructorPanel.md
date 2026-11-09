[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/InstructorPanel](../index.md) / InstructorPanel

# Function: InstructorPanel()

> **InstructorPanel**(`__namedParameters`): `Element`

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/InstructorPanel.tsx:149](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/calendar/instructor-dnd/InstructorPanel.tsx#L149)

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
