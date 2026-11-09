[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CalendarFilterProvider](../index.md) / usePaInstructorId

# Function: usePaInstructorId()

> **usePaInstructorId**(): `number`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:410](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/CalendarFilterProvider.tsx#L410)

The one instructor the פ"א view is about: the PA view's own instructor while
it is on, else whoever the instructor filter is narrowed to, else the
signed-in user. It used to be a hard-coded Hive id, so the "busy" dimming
was computed for a stranger and never matched the viewer.

## Returns

`number`
