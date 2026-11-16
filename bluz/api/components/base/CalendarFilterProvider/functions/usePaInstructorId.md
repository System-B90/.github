[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CalendarFilterProvider](../index.md) / usePaInstructorId

# Function: usePaInstructorId()

> **usePaInstructorId**(): `number`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:463](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/base/CalendarFilterProvider.tsx#L463)

The one instructor the פ"א view is about: the PA view's own instructor while
it is on, else whoever the instructor filter is narrowed to, else the
signed-in user. It used to be a hard-coded Hive id, so the "busy" dimming
was computed for a stranger and never matched the viewer.

## Returns

`number`
