[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/InstructorDndProvider](../index.md) / InstructorDndProvider

# Function: InstructorDndProvider()

> **InstructorDndProvider**(`props`): `Element`

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/InstructorDndProvider.tsx:83](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/instructor-dnd/InstructorDndProvider.tsx#L83)

Layers a

## Parameters

### props

`InstructorDndProviderProps`

Events in state plus the shared save callback.

## Returns

`Element`

The provider element wrapping the calendar subtree.

## Dnd-kit

drag context over the calendar so instructors can be
assigned by dropping them onto an event and unassigned by dragging their chip
out of it. react-big-calendar's own DnD addon keeps owning event *movement*:
the two never collide because every dnd-kit drag source stops pointer
propagation, and drop targets only register refs.
