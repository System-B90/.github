[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CalendarFilterProvider](../index.md) / usePaInstructorId

# Function: usePaInstructorId()

> **usePaInstructorId**(): `number`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:410](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/base/CalendarFilterProvider.tsx#L410)

The one instructor the פ"א view is about: the PA view's own instructor while
it is on, else whoever the instructor filter is narrowed to, else the
signed-in user. It used to be a hard-coded Hive id, so the "busy" dimming
was computed for a stranger and never matched the viewer.

## Returns

`number`
